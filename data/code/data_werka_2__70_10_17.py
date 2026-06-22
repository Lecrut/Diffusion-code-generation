def get_boundary_strings(input_list):
    if not input_list:
        raise ValueError("Input list must not be empty")
    return input_list[0], input_list[-1]

def process_with_metadata(data):
    labels = {"first": "start", "last": "end"}
    result = {}
    for key, label in labels.items():
        result[label] = data[key]
    return result

if __name__ == '__main__':
    sample_data = ["initial", "middle", "final"]
    first, last = get_boundary_strings(sample_data)
    metadata = process_with_metadata({"first": first, "last": last})
    print(metadata["start"])
    print(metadata["end"])