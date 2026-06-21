import re

def rle_compress_decompress(data):
    compressed = re.sub(r'(.)\1+', lambda m: str(len(m.group(0))) + m.group(0)[0], data)
    decompressed = re.sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), compressed)
    return compressed, decompressed

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    comp, decomp = rle_compress_decompress(sample_string)
    print(comp)
    print(decomp)