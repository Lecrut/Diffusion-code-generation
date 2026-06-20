def read_volumes_from_string(data):
    lines = data.strip().split('\n')
    volumes = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            value = float(line)
            volumes.append(value)
        except ValueError:
            continue
    return volumes

def calculate_total_volume(data):
    volumes = read_volumes_from_string(data)
    return sum(volumes)

if __name__ == '__main__':
    sample_data = "10.5\n20.0\ninvalid\n5.5\n30\n-2.5"
    total = calculate_total_volume(sample_data)
    print(total)