def is_unique_without_aux(s):
    if s is None:
        return False
    n = len(s)
    if n <= 1:
        return True
    chars = list(s)
    chars.sort()
    for i in range(1, n):
        if chars[i] == chars[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = "programming"
    result = is_unique_without_aux(sample_string)
    print(result)