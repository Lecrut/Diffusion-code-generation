def is_unique_sorted(s):
    if s is None or len(s) <= 1:
        return True
    chars = list(s)
    chars.sort()
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = "programming"
    result = is_unique_sorted(sample_string)
    print(result)