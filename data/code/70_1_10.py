def check_first_and_last(data):
    if not data:
        return None, None
    return data[0], data[-1]

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45]
    first_val, last_val = check_first_and_last(sample_list)
    print(f"First: {first_val}, Last: {last_val}")

    sample_single_element = [7]
    first_single, last_single = check_first_and_last(sample_single_element)
    print(f"First (single): {first_single}, Last (single): {last_single}")

    empty_sample = []
    first_empty, last_empty = check_first_and_last(empty_sample)
    print(f"First (empty): {first_empty}, Last (empty): {last_empty}")