def reverse_string(s):
    if not s:
        return ""
    return s[::-1]

if __name__ == '__main__':
    test_word = "AlibabaCloud"
    reversed_test_word = reverse_string(test_word)
    print(reversed_test_word)