def check_number(n):
    is_positive = n > 0
    is_even = n % 2 == 0
    is_less_than_100 = n < 100
    return {
        "is_positive": is_positive,
        "is_even": is_even,
        "is_less_than_100": is_less_than_100
    }

def process_inputs(values):
    results = []
    for val in values:
        try:
            num = int(val)
            results.append(check_number(num))
        except (ValueError, TypeError):
            results.append(None)
    return results

if __name__ == '__main__':
    sample_values = [50, -10, 105]
    output = process_inputs(sample_values)
    print(output)