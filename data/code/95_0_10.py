NUMERIC_PROPERTIES = {
    "positive": lambda n: n > 0,
    "even": lambda n: n % 2 == 0,
    "divisible_by_three": lambda n: n % 3 == 0
}

def evaluate_number(n):
    results = {}
    for key, checker in NUMERIC_PROPERTIES.items():
        results[key] = checker(n)
    return results

if __name__ == '__main__':
    samples = [12, 7, -3, 0]
    for val in samples:
        props = evaluate_number(val)
        print(f"{val}: {props}")