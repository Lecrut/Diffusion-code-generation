from itertools import groupby

def run_length_encode(s):
    if not s:
        return []
    result = []
    for key, group in groupby(s):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

def run_length_decode(encoded_list):
    result = []
    for char, count in encoded_list:
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    encoded = run_length_encode("aaabbccc")
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)