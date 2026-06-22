def parse_volumes(volume_string):
    volumes = []
    for value in volume_string.split(','):
        try:
            number = float(value)
            volumes.append(number)
        except ValueError:
            continue
    return volumes

if __name__ == '__main__':
    sample_input = "3.5,4.2,abc,5.0"
    result = parse_volumes(sample_input)
    print(result)