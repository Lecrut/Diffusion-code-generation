def reverse_word(s):
    char_list = list(s)
    left, right = 0, len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    return ''.join(char_list)

if __name__ == '__main__':
    sample_word1 = "Alibaba"
    reversed_sample1 = reverse_word(sample_word1)
    print(f"Original: {sample_word1}, Reversed: {reversed_sample1}")

    sample_word2 = "Cloud"
    reversed_sample2 = reverse_word(sample_word2)
    print(f"Original: {sample_word2}, Reversed: {reversed_sample2}")

    sample_word3 = "Qwen"
    reversed_sample3 = reverse_word(sample_word3)
    print(f"Original: {sample_word3}, Reversed: {reversed_sample3}")