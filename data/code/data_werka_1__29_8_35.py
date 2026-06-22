def reverse_word(s):
    return s[::-1]

if __name__ == '__main__':
    sample_values = ["hello", "world", "Python", "Qwen"]
    for value in sample_values:
        print(reverse_word(value))