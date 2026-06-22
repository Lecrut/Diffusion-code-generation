def validate_pairs(pairs):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in pairs):
        raise ValueError("All elements must be tuples of two numbers")

def calculate_averages(pairs):
    sum_firsts = sum(second for first, second in pairs)
    sum_seconds = sum(first for first, second in pairs)
    count = len(pairs)
    average_firsts = sum_firsts / count
    average_seconds = sum_seconds / count
    return {'first': average_firsts, 'second': average_seconds}

if __name__ == '__main__':
    pairs = [
        (10, 20),
        (5, 15),
        (8, 2),
        (12, 30)
    ]
    validate_pairs(pairs)
    result = calculate_averages(pairs)
    print(result)