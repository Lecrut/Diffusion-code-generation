def evaluate_integers(a, b, c):
    results = []
    for val in [a, b, c]:
        if not isinstance(val, int):
            raise ValueError(f"Expected integer, got {type(val)}")
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

if __name__ == '__main__':
    sample_values = [42, -3, 100]
    output = evaluate_integers(*sample_values)
    print(output)