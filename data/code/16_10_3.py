import sys

def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current_char = data[0]
    count = 1
    length = len(data)
    for i in range(1, length):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAABBB"
    result = run_length_encode(sample_string)
    print(result)