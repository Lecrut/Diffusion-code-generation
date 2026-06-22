def is_unique_sorted(s):
    if not s:
        return True
    sorted_s = "".join(sorted(s))
    for i in range(1, len(sorted_s)):
        if sorted_s[i] == sorted_s[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = "programming"
    result = is_unique_sorted(sample_string)
    print(result)
    sample_string_two = "abcdef"
    result_two = is_unique_sorted(sample_string_two)
    print(result_two)