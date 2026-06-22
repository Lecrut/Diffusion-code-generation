def total_length_of_strings(strings):
    if not isinstance(strings, list):
        raise ValueError("Input must be a list of strings")
    return sum(len(s) for s in strings)

if __name__ == '__main__':
    sample_values = ["hello", "world", "programming", "in", "python"]
    result = total_length_of_strings(sample_values)
    print(result)