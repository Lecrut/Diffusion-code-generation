REVERSE_SLICE = slice(None, None, -1)

def reverse_string(s):
    return s[REVERSE_SLICE]

if __name__ == '__main__':
    sample_string_short = "hello"
    reversed_short = reverse_string(sample_string_short)
    print(f"Original: {sample_string_short}, Reversed: {reversed_short}")
    sample_string_long = "this is a test string for optimization" * 1000
    reversed_long = reverse_string(sample_string_long)
    print(f"Original length: {len(sample_string_long)}")
    print(f"Reversed (first 50 chars): {reversed_long[:50]}...")