def parse_volumes(volume_string):
    volumes = []
    if not volume_string:
        return volumes
    parts = volume_string.split(',')
    for part in parts:
        try:
            volumes.append(float(part.strip()))
        except ValueError:
            pass
    return volumes
if __name__ == '__main__':
    sample_input = "10.5,20,invalid,33.1,40"
    result = parse_volumes(sample_input)
    print(result)