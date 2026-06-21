def is_unique_sorted(s):
    sorted_chars = sorted(s)
    for i in range(len(sorted_chars) - 1):
        if sorted_chars[i] == sorted_chars[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = "abcdefg"
    print(is_unique_sorted(sample_string))