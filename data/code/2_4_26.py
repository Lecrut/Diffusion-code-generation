def parse_volume_values(volume_string):
    try:
        volume_list = [float(value.strip()) for value in volume_string.split(',')]
        return volume_list
    except ValueError as e:
        print(f"Error parsing volume values: {e}")
        return []

if __name__ == '__main__':
    sample_input = "10.5, 20.3, abc, 30.7"
    result = parse_volume_values(sample_input)
    print(result)