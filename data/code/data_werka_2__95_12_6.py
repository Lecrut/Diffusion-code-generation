def process_integers(a, b, c):
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

if __name__ == '__main__':
    sample_values = [10, -5, 150]
    output = process_integers(*sample_values)
    print(output)