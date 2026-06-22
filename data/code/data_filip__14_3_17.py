def is_unique_chars(s):
    sorted_s = sorted(s)
    for i in range(len(sorted_s) - 1):
        if sorted_s[i] == sorted_s[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = is_unique_chars(sample_string)
    print(result)