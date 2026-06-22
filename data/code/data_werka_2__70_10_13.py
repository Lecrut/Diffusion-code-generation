def process_boundary_items(input_list):
    if not input_list:
        raise ValueError("Input list must not be empty")
    result_map = {
        "first": input_list[0],
        "last": input_list[-1]
    }
    return result_map

if __name__ == '__main__':
    sample_data = ["strawberry", "blueberry", "raspberry", "blackberry"]
    boundaries = process_boundary_items(sample_data)
    print(boundaries["first"])
    print(boundaries["last"])