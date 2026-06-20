def convert_volumes(file_path):
    results = []
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            try:
                value = float(parts[0])
                unit = parts[1].lower()
                if unit == 'ml':
                    liters = value / 1000.0
                elif unit == 'cl':
                    liters = value / 100.0
                elif unit == 'dl':
                    liters = value / 10.0
                elif unit == 'l':
                    liters = value
                elif unit == 'm3':
                    liters = value * 1000.0
                else:
                    continue
                cubic_meters = liters / 1000.0
                results.append((value, unit, liters, cubic_meters))
            except ValueError:
                continue
    except FileNotFoundError:
        results.append(f"Error: File '{file_path}' not found.")
    except IOError:
        results.append(f"Error: Could not read file '{file_path}'.")
    return results

if __name__ == '__main__':
    sample_content = """1000 ml
500 cl
2.5 l
0.001 m3"""
    with open('temp_volumes.txt', 'w') as f:
        f.write(sample_content)
    output = convert_volumes('temp_volumes.txt')
    for item in output:
        if isinstance(item, tuple):
            value, unit, l, m3 = item
            print(f"{value} {unit} = {l} liters = {m3} cubic meters")
        else:
            print(item)