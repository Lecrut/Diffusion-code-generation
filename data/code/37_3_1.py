import time
def combine_strings_plus(str1, str2):
    return str1 + str2
if __name__ == '__main__':
    string_a = "Hello, "
    string_b = "World!"
    start_time = time.perf_counter()
    result = combine_strings_plus(string_a, string_b)
    end_time = time.perf_counter()
    print(f"Result: {result}")
    print(f"Time taken: {(end_time - start_time):.6f} seconds")