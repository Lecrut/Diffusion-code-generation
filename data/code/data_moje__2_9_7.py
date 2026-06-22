import math

def read_volumes_from_string(file_content):
    total_volume = 0.0
    lines = file_content.strip().split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 2:
            continue
        try:
            radius = float(parts[0])
            height = float(parts[1])
            if radius <= 0 or height <= 0:
                continue
            volume = math.pi * (radius ** 2) * height
            total_volume += volume
        except ValueError:
            continue
    return total_volume

if __name__ == '__main__':
    sample_data = "5.0, 10.0\n3.0, 4.5\ninvalid, 2.0\n0, 5.0"
    result = read_volumes_from_string(sample_data)
    print(result)