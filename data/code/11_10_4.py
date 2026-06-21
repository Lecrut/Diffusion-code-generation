def find_repeated_chars(s):
    count_map = {}
    repeated = []
    for char in s:
        if char in count_map:
            count_map[char] += 1
            if count_map[char] == 2:
                repeated.append(char)
        else:
            count_map[char] = 1
    return repeated

if __name__ == '__main__':
    sample_string = "programming"
    result = find_repeated_chars(sample_string)
    print(result)