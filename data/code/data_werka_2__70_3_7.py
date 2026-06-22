def extract_boundary_values(number_list):
    if len(number_list) == 0:
        raise ValueError("Input list must contain at least one number")
    start_value = number_list[0]
    end_value = number_list[-1]
    return start_value, end_value

if __name__ == '__main__':
    raw_data = "7 14 21 28 35"
    parsed_values = [int(token) for token in raw_data.split()]
    left_endpoint, right_endpoint = extract_boundary_values(parsed_values)
    print(left_endpoint, right_endpoint)