def is_unique_characters(s):
    sorted_str = sorted(s)
    for i in range(1, len(sorted_str)):
        if sorted_str[i] == sorted_str[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = 'abcdefg'
    result = is_unique_characters(sample_string)
    print(result)