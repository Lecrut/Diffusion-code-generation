def convert_volumes(volume_strings):
    results = []
    for volume_str in volume_strings:
        try:
            volume_liter = float(volume_str)
        except ValueError:
            continue
        cubic_meters = volume_liter / 1000.0
        results.append((volume_liter, cubic_meters))
    return results

def read_and_convert_volumes(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return []
    except IOError:
        return []

    volume_strings = [line.strip() for line in lines if line.strip()]
    return convert_volumes(volume_strings)

if __name__ == '__main__':
    sample_volumes = ["1.5", "250", "0.001", "invalid", "1000"]
    converted = convert_volumes(sample_volumes)
    for liter, cubic_meter in converted:
        print(f"{liter} liters = {cubic_meter} cubic meters")