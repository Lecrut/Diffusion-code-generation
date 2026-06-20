def convert_measurements(values):
    results = []
    for value in values:
        meters = value * 1000
        feet = meters * 3.28084
        results.append((meters, feet))
    return results

if __name__ == '__main__':
    sample_values = [1.5, 2.0, 0.75]
    converted = convert_measurements(sample_values)
    for original, (meters, feet) in zip(sample_values, converted):
        print(f"{original} km -> {meters:.2f} m, {feet:.2f} ft")