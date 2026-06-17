def check_positivity(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    samples = [10.5, -3.2, 0, 42]
    results = []
    for sample in samples:
        is_positive = check_positivity(sample)
        results.append((sample, is_positive))
    print(results)