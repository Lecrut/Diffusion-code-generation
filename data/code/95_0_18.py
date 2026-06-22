def analyze_number(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    positive = n > 0
    even = n % 2 == 0
    divisible_by_three = n % 3 == 0
    return {
        "value": n,
        "positive": positive,
        "even": even,
        "divisible_by_three": divisible_by_three
    }

if __name__ == '__main__':
    results = []
    for val in [12, -6, 7, 0, 15]:
        results.append(analyze_number(val))
    for r in results:
        print(r)