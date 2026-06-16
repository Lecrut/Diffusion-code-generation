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
    result1 = direct_comparison(string1, string2)
    time1 = time.perf_counter() - start_time
    result2 = len(string1) == len(string2)
    time2 = time.perf_counter() - start_time
    result3 = manual_iteration_comparison(string1, string2)
    time3 = time.perf_counter() - start_time
    print(f"String Length: {STRING_LENGTH}")
    print("-" * 30)
    print(f"Method 1 (Direct comparison of len()): Result={result1}, Time={time1:.6f}s")
    print(f"Method 2 (len() comparison): Result={result2}, Time={time2:.6f}s")
    print(f"Method 3 (Manual iteration): Result={result3}, Time={time3:.6f}s")
if __name__ == '__main__':
    benchmark()