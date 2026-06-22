def check_values(a, b, c):
    results = []
    for val in [a, b, c]:
        is_positive = val > 0
        is_even = val % 2 == 0
        is_less_than_100 = val < 100
        results.append({
            'value': val,
            'is_positive': is_positive,
            'is_even': is_even,
            'is_less_than_100': is_less_than_100
        })
    return results

def get_integer_input(prompt):
    try:
        value = int(prompt)
        return value
    except ValueError:
        raise ValueError(f"Invalid integer input: {prompt}")

if __name__ == '__main__':
    sample_inputs = [10, 20, 30]
    results = check_values(*sample_inputs)
    for res in results:
        print(res)