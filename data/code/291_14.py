import time
def create_long_string(length):
    return "a" * length
def direct_comparison(s1, s2):
    return len(s1) == len(s2)
def len_function_comparison(s1, s2):
    return len(s1) == len(s2)
def manual_iteration_comparison(s1, s2):
    len1 = 0
    for char in s1:
        len1 += 1
    len2 = 0
    for char in s2:
        len2 += 1
    return len1 == len2
STRING_LENGTH = 1000000
string1 = create_long_string(STRING_LENGTH)
string2 = create_long_string(STRING_LENGTH)
def benchmark():
    start_time = time.perf_counter()
    result_direct = direct_comparison(string1, string2)
    end_time = time.perf_counter()
    time_direct = end_time - start_time
    start_time = time.perf_counter()
    result_len = len_function_comparison(string1, string2)
    end_time = time.perf_counter()
    time_len = end_time - start_time
    start_time = time.perf_counter()
    result_manual = manual_iteration_comparison(string1, string2)
    end_time = time.perf_counter()
    time_manual = end_time - start_time
    print(f"String Length: {STRING_LENGTH}")
    print("-" * 30)
    print(f"Direct Comparison (len()): Result={result_direct}, Time={time_direct:.6f} seconds")
    print(f"Built-in len() Comparison: Result={result_len}, Time={time_len:.6f} seconds")
    print(f"Manual Iteration Comparison: Result={result_manual}, Time={time_manual:.6f} seconds")
if __name__ == '__main__':
    benchmark()