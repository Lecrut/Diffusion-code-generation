def parse_volumes(input_string):
    volumes = []
    if not input_string:
        return volumes
    parts = input_string.split(',')
    for part in parts:
        part = part.strip()
        if not part:
            continue
        try:
            volume = float(part)
            volumes.append(volume)
        except ValueError:
            continue
    return volumes
if __name__ == '__main__':
    sample_input_1 = "10.5,20,invalid,33.33"
    result_1 = parse_volumes(sample_input_1)
    print(result_1)
    sample_input_2 = "1,2,3,4"
    result_2 = parse_volumes(sample_input_2)
    print(result_2)
    sample_input_3 = "abc,100,xyz,200.5"
    result_3 = parse_volumes(sample_input_3)
    print(result_3)
    sample_input_4 = ""
    result_4 = parse_volumes(sample_input_4)
    print(result_4)
    sample_input_5 = "1.1,2.2,3.3"
    result_5 = parse_volumes(sample_input_5)
    print(result_5)