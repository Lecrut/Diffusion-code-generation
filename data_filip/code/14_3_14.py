def check_unique_by_sorting(s):
    chars = list(s)
    chars.sort()
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = check_unique_by_sorting(sample_string)
    print(result)