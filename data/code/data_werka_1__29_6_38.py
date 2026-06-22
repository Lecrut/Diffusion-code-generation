def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    SAMPLE_WORD = "Qwen"
    REVERSED_SAMPLE = reverse_string(SAMPLE_WORD)
    print(REVERSED_SAMPLE)