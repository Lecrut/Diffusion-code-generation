def parse_volumes(volume_string):
    volumes = []
    for value in volume_string.split(','):
        try:
            volumes.append(float(value))
        except ValueError:
            print(f"Warning: '{value}' is not a valid number and will be ignored.")
    return volumes

if __name__ == '__main__':
    sample_input = "3.5,4.2,invalid,7.8"
    parsed_volumes = parse_volumes(sample_input)
    print(parsed_volumes)