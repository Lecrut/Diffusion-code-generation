def get_boundary_elements(data_stream):
    if not data_stream:
        raise ValueError("Data stream cannot be empty")
    boundary_map = {"start": 0, "end": -1}
    first_val = data_stream[boundary_map["start"]]
    last_val = data_stream[boundary_map["end"]]
    return first_val, last_val

if __name__ == '__main__':
    raw_sequence = "5 12 19 26 33"
    parsed_numbers = list(map(int, raw_sequence.split()))
    head, tail = get_boundary_elements(parsed_numbers)
    print(head, tail)