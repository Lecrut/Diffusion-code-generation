def process_boundary_items(text_list):
    if not isinstance(text_list, (list, tuple)):
        raise ValueError("Input must be a sequence")
    if len(text_list) == 0:
        raise ValueError("Sequence cannot be empty")
    result_map = {"first": text_list[0], "last": text_list[-1]}
    return result_map

if __name__ == '__main__':
    sample_data = ["initial", "middle_1", "middle_2", "final"]
    output = process_boundary_items(sample_data)
    print(output["first"])
    print(output["last"])