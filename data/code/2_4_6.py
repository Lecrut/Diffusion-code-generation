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
            pass
    return volumes
if __name__ == '__main__':
    sample_input_1 = "10.5,20,30.7,invalid,40"
    sample_input_2 = "5.0,15.2,error,25.5"
    sample_input_3 = ""
    sample_input_4 = "1,2,3,4"
    print("--- Testing Sample 1 ---")
    result_1 = parse_volumes(sample_input_1)
    print(result_1)
    print("\n--- Testing Sample 2 ---")
    result_2 = parse_volumes(sample_input_2)
    print(result_2)
    print("\n--- Testing Sample 3 (Empty String) ---")
    result_3 = parse_volumes(sample_input_3)
    print(result_3)
    print("\n--- Testing Sample 4 ---")
    result_4 = parse_volumes(sample_input_4)
    print(result_4)