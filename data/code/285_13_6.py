def compare_adjacent_strings(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    
    return [max(pair) for pair in zip(strings, strings[1:])]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    result = compare_adjacent_strings(sample_values)
    print(result)