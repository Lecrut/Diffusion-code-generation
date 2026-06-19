REVERSE_STR = lambda s: s[::-1]

if __name__ == '__main__':
    SAMPLE_STRING = "Hello, World!"
    REVERSED_STRING = REVERSE_STR(SAMPLE_STRING)
    print(f"Original: {SAMPLE_STRING}")
    print(f"Reversed: {REVERSED_STRING}")