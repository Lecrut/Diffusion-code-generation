def reverse_word(s):
    char_list = list(s)
    left, right = 0, len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    return ''.join(char_list)

if __name__ == '__main__':
    test_cases = {
        "hello": "olleh",
        "world": "dlrow",
        "Python": "nohtyP"
    }
    
    for original, expected in test_cases.items():
        result = reverse_word(original)
        print(f"Original: {original}, Reversed: {result}")