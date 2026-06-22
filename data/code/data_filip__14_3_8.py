def is_unique_sorted(s):
    chars = sorted(s)
    for i in range(len(chars) - 1):
        if chars[i] == chars[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample = "abcdefg"
    print(is_unique_sorted(sample))
    sample2 = "hello"
    print(is_unique_sorted(sample2))