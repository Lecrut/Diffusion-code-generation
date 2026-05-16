import time
def combine_strings_plus(s1: str, s2: str) -> str:
    return s1 + s2
if __name__ == '__main__':
    string1 = "Hello, "
    string2 = "World!"
    start_time = time.perf_counter()
    result = combine_strings_plus(string1, string2)
    end_time = time.perf_counter()
    print(f"Result: {result}")
    print(f"Execution time: {(end_time - start_time):.6f} seconds")