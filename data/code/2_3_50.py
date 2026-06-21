def parse_volumes(volume_string):
    volumes = volume_string.split(',')
    result = []
    for volume in volumes:
        try:
            number = float(volume.strip())
            result.append(number)
        except ValueError:
            print(f"Warning: '{volume}' is not a valid number and will be skipped.")
    return result

if __name__ == '__main__':
    sample_input = "3.14, 2.718, abc, 0.999, 5"
    parsed_volumes = parse_volumes(sample_input)
    print(parsed_volumes)