import time
def reverse_string(s):
    return s[::-1]
if __name__ == '__main__':
    sample_string_short = "hello"
    reversed_short = reverse_string(sample_string_short)
    print(f"Original: {sample_string_short}, Reversed: {reversed_short}")
    sample_string_long = "this is a test string for optimization" * 10000
    start_time = time.perf_counter()
    reversed_long = reverse_string(sample_string_long)
    end_time = time.perf_counter()
    print(f"Original length: {len(sample_string_long)}")
    print(f"Reversed (first 50 chars): {reversed_long[:50]}...")
    print(f"Time taken for long string: {end_time - start_time:.6f} seconds")