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
    text_to_scan = "abababaabab"
    substring_to_find = "aba"
    start_time = time.time()
    result = find_all_occurrences(text_to_scan, substring_to_find)
    end_time = time.time()
    print(f"Text: {text_to_scan}")
    print(f"Substring: {substring_to_find}")
    print(f"Starting indices: {result}")
    print(f"Time taken: {end_time - start_time} seconds")
    text_to_scan_2 = "aaaaa"
    substring_to_find_2 = "aa"
    start_time_2 = time.time()
    result_2 = find_all_occurrences(text_to_scan_2, substring_to_find_2)
    end_time_2 = time.time()
    print(f"\nText: {text_to_scan_2}")
    print(f"Substring: {substring_to_find_2}")
    print(f"Starting indices: {result_2}")
    print(f"Time taken: {end_time_2 - start_time_2} seconds")