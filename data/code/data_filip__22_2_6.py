import re

def decompress_rle(encoded_str):
    pairs = re.findall(r'(\d+)(\D)', encoded_str)
    return ''.join(count * char for count, char in pairs)

if __name__ == '__main__':
    encoded_sample1 = '2a3b4c'
    decoded_sample1 = decompress_rle(encoded_sample1)
    print(decoded_sample1)

    encoded_sample2 = '10x2y'
    decoded_sample2 = decompress_rle(encoded_sample2)
    print(decoded_sample2)

    encoded_sample3 = '1a1b1c'
    decoded_sample3 = decompress_rle(encoded_sample3)
    print(decoded_sample3)