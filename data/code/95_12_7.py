def process_integers(a, b, c):
    results = []
    for val in (a, b, c):
        checks = []
        if val > 0:
            checks.append("positive")
        if val % 2 == 0:
            checks.append("even")
        if val < 100:
            checks.append("less_than_100")
        results.append({
            "value": val,
            "checks": checks
        })
    return results

if __name__ == '__main__':
    sample_values = [10, 200, -5]
    output = process_integers(*sample_values)
    for item in output:
        print(item)