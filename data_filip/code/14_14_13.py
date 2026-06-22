def has_unique_chars(s: str) -> bool:
    sorted_str = ''.join(sorted(s))
    for i in range(len(sorted_str) - 1):
        if sorted_str[i] == sorted_str[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = has_unique_chars(sample_string)
    print(result)