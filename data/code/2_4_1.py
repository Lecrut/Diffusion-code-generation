def parse_volumes(volume_string):
    volumes = []
    if not volume_string:
        return volumes
    parts = volume_string.split(',')
    for part in parts:
        try:
            volumes.append(float(part.strip()))
        except ValueError:
            continue
    return volumes
if __name__ == '__main__':
    sample_input_1 = "10.5,20,30.7,invalid,40"
    result_1 = parse_volumes(sample_input_1)
    print(result_1)
    sample_input_2 = "5.0,15.5,25.0"
    result_2 = parse_volumes(sample_input_2)
    print(result_2)
    sample_input_3 = "abc,10,xyz,20"
    result_3 = parse_volumes(sample_input_3)
    print(result_3)
    sample_input_4 = ""
    result_4 = parse_volumes(sample_input_4)
    print(result_4)