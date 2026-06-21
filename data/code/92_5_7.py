def flip_truth_values(source):
    valid_types = (bool,)
    for item in source:
        if not isinstance(item, valid_types):
            raise ValueError("Input must contain boolean values")
        yield not item

def process_data(data):
    return list(flip_truth_values(data))

if __name__ == '__main__':
    test_set = [True, False, False, True, True]
    output = process_data(test_set)
    print(output)