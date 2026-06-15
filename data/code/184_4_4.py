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
    large_string = "abababaabababa" * 10000
    substring = "aba"
    start_time = time.time()
    result = find_all_occurrences(large_string, substring)
    end_time = time.time()
    print(f"String: {large_string[:50]}...")
    print(f"Substring: {substring}")
    print(f"Starting indices: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")