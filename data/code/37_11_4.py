import time
def combine_strings(str1, str2):
    return str1 + str2
if __name__ == '__main__':
    string_a = "Hello, "
    string_b = "World!"
    start_time = time.perf_counter()
    result = combine_strings(string_a, string_b)
    end_time = time.perf_counter()
    print(result)
    print(f"Execution time: {(end_time - start_time) * 1e6:.3f} microseconds")