def validate_pairs(pairs):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in pairs):
        raise ValueError("All elements must be tuples of exactly two floating-point numbers")

def calculate_pair_averages(pairs):
    validate_pairs(pairs)
    sum_first = sum(second for first, second in pairs)
    sum_second = sum(first for first, second in pairs)
    count = len(pairs)
    avg_first = sum_first / count if count > 0 else None
    avg_second = sum_second / count if count > 0 else None
    return {"first_average": avg_first, "second_average": avg_second}

if __name__ == '__main__':
    sample_data = [(1.5, 2.5), (3.5, 4.5), (5.5, 6.5)]
    result = calculate_pair_averages(sample_data)
    print(result)