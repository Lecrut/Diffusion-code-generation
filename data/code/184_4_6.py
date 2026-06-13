import time
def find_all_occurrences(text, pattern):
    indices = []
    n = len(text)
    m = len(pattern)
    if m == 0:
        return list(range(n + 1))
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            indices.append(i)
    return indices
if __name__ == '__main__':
    large_string = "abababaabababa"
    substring = "aba"
    start_time = time.time()
    result = find_all_occurrences(large_string, substring)
    end_time = time.time()
    print(f"String: {large_string}")
    print(f"Substring: {substring}")
    print(f"Indices of occurrences: {result}")
    print(f"Time taken: {end_time - start_time} seconds")
    large_string_2 = "aaaaaaaaaaaaaaaaaa"
    substring_2 = "aaa"
    start_time_2 = time.time()
    result_2 = find_all_occurrences(large_string_2, substring_2)
    end_time_2 = time.time()
    print(f"\nString: {large_string_2}")
    print(f"Substring: {substring_2}")
    print(f"Indices of occurrences: {result_2}")
    print(f"Time taken: {end_time_2 - start_time_2} seconds")