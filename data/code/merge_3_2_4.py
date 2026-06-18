def parse_volumes(volume_string):
    result = []
    if not volume_string:
        return result
    volumes = volume_string.split(',')
    for vol_str in volumes:
        vol_str = vol_str.strip()
        if not vol_str:
            continue
        try:
            result.append(float(vol_str))
        except ValueError:
            print(f"Error: Could not convert '{vol_str}' to a float.")
            pass
    return result
if __name__ == '__main__':
    sample_input_1 = "10.5,20,33.14"
    sample_input_2 = "5.0,invalid,12.7"
    sample_input_3 = "1,2,three,4.5"
    sample_input_4 = ""
    print(f"Input: '{sample_input_1}'")
    print("Output:", parse_volumes(sample_input_1))
    print("-" * 20)
    print(f"Input: '{sample_input_2}'")
    print("Output:", parse_volumes(sample_input_2))
    print("-" * 20)
    print(f"Input: '{sample_input_3}'")
    print("Output:", parse_volumes(sample_input_3))
    print("-" * 20)
    print(f"Input: '{sample_input_4}'")
    print("Output:", parse_volumes(sample_input_4))