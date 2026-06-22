def km_to_m(km):
    return km * 1000

def format_table(test_cases):
    lines = []
    lines.append(f"{'Kilometers':<15} {'Meters':<15}")
    lines.append("-" * 30)
    for km in test_cases:
        meters = km_to_m(km)
        lines.append(f"{km:<15.2f} {meters:<15.2f}")
    return "\n".join(lines)

if __name__ == '__main__':
    test_kilometers = [1.5, 10, 0.25, 100, 0.001]
    output = format_table(test_kilometers)
    print(output)