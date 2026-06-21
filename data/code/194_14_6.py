def find_longest_string(strings):
    max_length = 0
    longest = ""
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest = string
    return longest

if __name__ == '__main__':
    sample_data = [
        "apple",
        "banana",
        "kiwi"
    ]
    result = find_longest_string(sample_data)
    print(result)