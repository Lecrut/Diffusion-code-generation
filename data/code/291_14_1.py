import time
def create_long_string(length):
    return "a" * length
def direct_comparison(s1, s2):
    return len(s1) == len(s2)
def built_in_len_comparison(s1, s2):
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
    result2 = built_in_len_comparison(string1, string2)
    time2 = time.perf_counter() - start_time
    result3 = manual_iteration_comparison(string1, string2)
    time3 = time.perf_counter() - start_time
    print(f"String Length: {STRING_LENGTH}")
    print("-" * 30)
    print(f"Direct Comparison Time: {time1:.6f} seconds (Result: {result1})")
    print(f"Built-in len() Comparison Time: {time2:.6f} seconds (Result: {result2})")
    print(f"Manual Iteration Comparison Time: {time3:.6f} seconds (Result: {result3})")
if __name__ == '__main__':
    benchmark()