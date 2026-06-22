def convert_measurements(measurements):
    results = []
    for value in measurements:
        meters = value * 1000
        feet = meters * 3.28084
        results.append((value, meters, feet))
    return results

def print_conversions(results):
    for original, meters, feet in results:
        print(f"{original} km = {meters:.2f} m = {feet:.2f} ft")

if __name__ == '__main__':
    sample_values = [1.5, 10, 0.25, 100]
    conversions = convert_measurements(sample_values)
    print_conversions(conversions)