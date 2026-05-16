def parse_volumes(volume_string):
    volumes = []
    if not volume_string:
        return volumes
    volume_list = volume_string.split(',')
    for item in volume_list:
        item = item.strip()
        if not item:
            continue
        try:
            volume = float(item)
            volumes.append(volume)
        except ValueError:
            print(f"Error: Could not convert '{item}' to a float.")
            continue
    return volumes
if __name__ == '__main__':
    sample_input_1 = "10.5,20,33.14"
    sample_input_2 = "5,hello,12.9"
    sample_input_3 = ""
    sample_input_4 = "1,2,three,4.5"
    print(f"Input: '{sample_input_1}'")
    result_1 = parse_volumes(sample_input_1)
    print(f"Result: {result_1}\n")
    print(f"Input: '{sample_input_2}'")
    result_2 = parse_volumes(sample_input_2)
    print(f"Result: {result_2}\n")
    print(f"Input: '{sample_input_3}'")
    result_3 = parse_volumes(sample_input_3)
    print(f"Result: {result_3}\n")
    print(f"Input: '{sample_input_4}'")
    result_4 = parse_volumes(sample_input_4)
    print(f"Result: {result_4}\n")