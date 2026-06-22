def parse_volumes(volume_string):
    volumes = volume_string.split(',')
    result = []
    for volume in volumes:
        try:
            value = float(volume)
            result.append(value)
        except ValueError:
            raise ValueError(f"Invalid volume value: {volume}")
    return result

if __name__ == '__main__':
    sample_input = "10.5,20.3,abc,30.7"
    try:
        parsed_volumes = parse_volumes(sample_input)
        print(parsed_volumes)
    except ValueError as e:
        print(e)