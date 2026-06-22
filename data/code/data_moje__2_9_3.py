def calculate_total_volume(filename):
    total_volume = 0.0
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        volume = float(line)
                        total_volume += volume
                    except ValueError:
                        continue
    except FileNotFoundError:
        return None
    return total_volume

def calculate_total_volume_from_list(volumes):
    total_volume = 0.0
    for item in volumes:
        try:
            volume = float(item)
            total_volume += volume
        except (ValueError, TypeError):
            continue
    return total_volume

if __name__ == '__main__':
    sample_volumes = ["10.5", "20.3", "invalid", "30.2", "", "abc", "5.0"]
    total = calculate_total_volume_from_list(sample_volumes)
    print(total)