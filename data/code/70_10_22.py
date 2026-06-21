FIRST_INDEX = 0
LAST_INDEX = -1

def get_boundary_strings(input_list):
    if not input_list:
        raise ValueError("Input list must not be empty")
    return input_list[FIRST_INDEX], input_list[LAST_INDEX]

if __name__ == '__main__':
    sample_data = ["start", "middle", "end"]
    first_str, last_str = get_boundary_strings(sample_data)
    print(first_str)
    print(last_str)