import sys

def decode_rle(encoded_list):
    result = []
    for item in encoded_list:
        count = item[0]
        char = item[1]
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_data = [(4, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]
    print(decode_rle(sample_data))