import tempfile
import os

def convert_volume_measurements(input_file_path):
    liters_per_cubic_meter = 1000.0
    results = []
    try:
        with open(input_file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return [("Error", "File not found: " + input_file_path)]
    except IOError as e:
        return [("Error", "IO error reading file: " + str(e))]
    except Exception as e:
        return [("Error", "Unexpected error: " + str(e))]

    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            volume = float(stripped)
            liters = volume
            cubic_meters = volume / liters_per_cubic_meter
            results.append((volume, liters, cubic_meters))
        except ValueError:
            results.append(("Error at line " + str(line_num), "Invalid number: " + stripped))

    return results

def print_volume_conversions(results):
    if not results:
        print("No data to display.")
        return

    print(f"{'Original':<12} {'Liters':<12} {'Cubic Meters':<15}")
    print("-" * 40)
    for item in results:
        if isinstance(item[0], str):
            print(f"{item[0]:<12} {item[1]}")
        else:
            original, liters, cubic_meters = item
            print(f"{original:<12.4f} {liters:<12.4f} {cubic_meters:<15.6f}")

def main():
    sample_data = [
        "1.5",
        "100",
        "0.001",
        "-50",
        "abc",
        "123.456",
        "",
        "999.999"
    ]

    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        temp_file_path = f.name
        f.write('\n'.join(sample_data))

    try:
        results = convert_volume_measurements(temp_file_path)
        print_volume_conversions(results)
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

if __name__ == '__main__':
    main()