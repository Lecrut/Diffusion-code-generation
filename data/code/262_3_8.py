def find_extremes_by_length(strings):
    if not strings:
        return None, None
    smallest = min(strings, key=len)
    largest = max(strings, key=len)
    return smallest, largest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    smallest, largest = find_extremes_by_length(sample_strings)
    print(f"Smallest: {smallest}, Largest: {largest}")