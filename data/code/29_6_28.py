def reverse_string(s):
    if not s:
        return ""
    return s[::-1]

if __name__ == '__main__':
    test_word = "Qwen"
    result = reverse_string(test_word)
    print(result)