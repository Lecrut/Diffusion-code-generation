def process_volumes(input_filename, sample_values):
    results = []
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                try:
                    value = float(line)
                    liters = value * 3.78541
                    cubic_meters = value * 0.00378541
                    results.append((value, liters, cubic_meters))
                except ValueError:
                    continue
    except FileNotFoundError:
        for value in sample_values:
            liters = value * 3.78541
            cubic_meters = value * 0.00378541
            results.append((value, liters, cubic_meters))
    except IOError:
        for value in sample_values:
            liters = value * 3.78541
            cubic_meters = value * 0.00378541
            results.append((value, liters, cubic_meters))

    output_lines = []
    for val, lit, cm in results:
        output_lines.append(f"Original: {val}, Liters: {lit:.4f}, Cubic Meters: {cm:.6f}")
    return "\n".join(output_lines)

if __name__ == '__main__':
    input_file_name = "volumes.txt"
    sample_data = [10.0, 25.5, 100.0, -5.0, 0.0]
    output_result = process_volumes(input_file_name, sample_data)
    print(output_result)