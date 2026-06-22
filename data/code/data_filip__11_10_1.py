def get_repeated_characters(s):
    frequency_map = {}
    repeated = []
    for char in s:
        if char in frequency_map:
            if frequency_map[char] == 1:
                repeated.append(char)
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1
    return repeated

if __name__ == '__main__':
    sample_string = "programming"
    result = get_repeated_characters(sample_string)
    print(result)