def check_number(n):
    is_positive = n > 0
    is_even = n % 2 == 0
    is_less_than_100 = n < 100
    return {
        'positive': is_positive,
        'even': is_even,
        'less_than_100': is_less_than_100
    }

def process_numbers(numbers):
    results = []
    for n in numbers:
        if not isinstance(n, int):
            raise ValueError(f"Input must be an integer, got {type(n).__name__}")
        results.append(check_number(n))
    return results

if __name__ == '__main__':
    sample_inputs = [50, -10, 105]
    output = process_numbers(sample_inputs)
    print(output)