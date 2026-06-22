def calculate_averages(pairs):
    first_elements = (float(pair[0]) for pair in pairs if len(pair) == 2)
    second_elements = (float(pair[1]) for pair in pairs if len(pair) == 2)

    avg_first = sum(first_elements) / len(list(first_elements)) if list(first_elements) else None
    avg_second = sum(second_elements) / len(list(second_elements)) if list(second_elements) else None

    return avg_first, avg_second

if __name__ == '__main__':
    sample_pairs = [
        (10, 20),
        (30, 40),
        ('a', 50),
        (60, 'b'),
        (70, 80)
    ]
    result = calculate_averages(sample_pairs)
    print(f"Average of the first elements: {result[0]}")
    print(f"Average of the second elements: {result[1]}")