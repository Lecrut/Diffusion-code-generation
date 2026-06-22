def read_volumes_from_file(file_path):
    volumes = []
    with open(file_path, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                try:
                    volumes.append(float(stripped))
                except ValueError:
                    continue
    return volumes

def calculate_total_volume(file_path):
    volumes = read_volumes_from_file(file_path)
    return sum(volumes)

def write_temp_file():
    import tempfile
    import os
    fd, path = tempfile.mkstemp(suffix='.txt')
    with os.fdopen(fd, 'w') as f:
        f.write('10.5\n20.3\nabc\n15.2\n-5.0\n')
    return path

if __name__ == '__main__':
    temp_file_path = write_temp_file()
    try:
        total = calculate_total_volume(temp_file_path)
        print(total)
    finally:
        import os
        os.remove(temp_file_path)