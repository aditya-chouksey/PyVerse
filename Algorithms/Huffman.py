import heapq
from collections import defaultdict, Counter

# Node class for Huffman Tree
class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char        # Character
        self.freq = freq        # Frequency of character
        self.left = None        # Left child
        self.right = None       # Right child

    # For priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(text):
    frequency = Counter(text)  # Count frequency of each character
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)        # Min-heap based on frequency

    while len(heap) > 1:
        # Pop two nodes with smallest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Merge them into a new node
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)  # Push merged node back to heap

    return heap[0]  # Root of Huffman Tree

# Function to generate Huffman Codes
def generate_codes(node, current_code="", codes={}):
    if node is None:
        return

    # If leaf node, assign code
    if node.char is not None:
        codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

    return codes

# Function to encode text
def huffman_encode(text, codes):
    return ''.join(codes[char] for char in text)

# Function to decode text
def huffman_decode(encoded_text, root):
    decoded_text = ""
    current = root
    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_text += current.char
            current = root

    return decoded_text

# Example Usage
if __name__ == "__main__":
    text = "huffman coding in python"
    root = build_huffman_tree(text)
    codes = generate_codes(root)

    print("Huffman Codes:", codes)

    encoded_text = huffman_encode(text, codes)
    print("Encoded Text:", encoded_text)

    decoded_text = huffman_decode(encoded_text, root)
    print("Decoded Text:", decoded_text)
