def calculate_total_length(strings):
    total_length = 0
    for string in strings:
        total_length += len(string)
    return total_length

if __name__ == '__main__':
    SAMPLE_STRINGS = ["hello", "world", "this", "is", "a", "test"]
    result = calculate_total_length(SAMPLE_STRINGS)
    print(result)