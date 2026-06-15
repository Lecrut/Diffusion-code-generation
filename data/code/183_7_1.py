def flatten_names(list_of_strings):
    flattened_list = []
    for line in list_of_strings:
        names = line.split()
        flattened_list.extend(names)
    return flattened_list
if __name__ == '__main__':
    sample_input = [
        "Alice Bob Charlie",
        "David Eve Frank",
        "Grace Henry"
    ]
    result = flatten_names(sample_input)
    print(result)