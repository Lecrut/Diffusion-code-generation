def convert_km_to_m(kilometers):
    return kilometers * 1000

def format_table(results):
    header = f"{'Kilometers':>15} | {'Meters':>15}"
    separator = '-' * len(header)
    print(header)
    print(separator)
    for km, m in results:
        line = f"{km:>15} | {m:>15}"
        print(line)

if __name__ == '__main__':
    test_cases = [1.5, 10, 0, 50.25]
    results = []
    for km in test_cases:
        m = convert_km_to_m(km)
        results.append((km, m))
    format_table(results)