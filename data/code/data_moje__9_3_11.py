def convert_volumes(input_data):
    results = []
    for item in input_data:
        try:
            value = float(item)
            if value < 0:
                results.append((value, "Error: Negative value", "Error: Negative value"))
                continue
            liters = value
            cubic_meters = value / 1000.0
            results.append((value, liters, cubic_meters))
        except ValueError:
            results.append((item, "Error: Invalid number", "Error: Invalid number"))
    return results

if __name__ == '__main__':
    sample_values = [100, 2500, 5000, "abc", -10]
    output = convert_volumes(sample_values)
    for original, l, m3 in output:
        print(f"Original: {original}, Liters: {l}, Cubic Meters: {m3}")