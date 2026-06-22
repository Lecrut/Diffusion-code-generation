def km_to_m(kilometers):
    return kilometers * 1000

def format_table(rows):
    header = "{:<15} | {:<10}".format("Kilometers", "Meters")
    separator = "-" * len(header)
    lines = [header, separator]
    for km, m in rows:
        lines.append("{:<15} | {:<10}".format(km, m))
    return "\n".join(lines)

if __name__ == '__main__':
    test_cases = [1, 2.5, 0, 100, 0.1]
    results = []
    for km in test_cases:
        meters = km_to_m(km)
        results.append((km, meters))
    print(format_table(results))