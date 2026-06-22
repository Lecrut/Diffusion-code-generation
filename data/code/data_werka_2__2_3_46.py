def parse_volumes(volume_string):
    volumes = volume_string.split(',')
    result = []
    for volume in volumes:
        try:
            value = float(volume.strip())
            result.append(value)
        except ValueError:
            print(f"Warning: '{volume}' is not a valid number and will be skipped.")
    return result

if __name__ == '__main__':
    sample_input = "3.5, 4.2, invalid, 7.8"
    parsed_volumes = parse_volumes(sample_input)
    print(parsed_volumes)