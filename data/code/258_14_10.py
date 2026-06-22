def calculate_averages(pairs):
    first_values = (float(a) for a, _ in pairs if isinstance(a, (int, float)))
    second_values = (float(b) for _, b in pairs if isinstance(b, (int, float)))
    
    avg_first = sum(first_values) / len(list(first_values)) if first_values else 0
    avg_second = sum(second_values) / len(list(second_values)) if second_values else 0
    
    return avg_first, avg_second

if __name__ == '__main__':
    sample_pairs = [
        (10, 20),
        (30, 'a'),
        ('b', 40),
        (50, 60)
    ]
    
    result = calculate_averages(sample_pairs)
    print(f"Average of the first elements: {result[0]}")
    print(f"Average of the second elements: {result[1]}")