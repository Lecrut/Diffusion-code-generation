def decompress_rle(encoded_string):
    result = []
    i = 0
    n = len(encoded_string)
    while i < n:
        count_start = i
        while i < n and encoded_string[i].isdigit():
            i += 1
        count = int(encoded_string[count_start:i])
        if i < n:
            char = encoded_string[i]
            result.append(char * count)
            i += 1
    return ''.join(result)
if __name__ == '__main__':
    test_cases = ['3A2B1C', '10A5B', '1X', '99Z', '', '1234567890A']
    for test in test_cases:
        result = decompress_rle(test)
        print(result)