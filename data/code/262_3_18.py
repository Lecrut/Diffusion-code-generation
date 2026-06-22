def find_min_max_by_length(strings):
    if not strings:
        raise ValueError("Input list cannot be empty")
    min_str = min(strings, key=len)
    max_str = max(strings, key=len)
    return min_str, max_str

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    min_str, max_str = find_min_max_by_length(sample_data)
    print(f"Shortest string: {min_str}")
    print(f"Longest string: {max_str}")