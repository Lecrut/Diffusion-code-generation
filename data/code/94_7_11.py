def has_truthy_element(source):
    truth_counter = 0
    for element in source:
        if element:
            truth_counter += 1
    return truth_counter > 0

if __name__ == '__main__':
    test_data = [0, 0.0, "", None, [], {}, False, 1, "hello", [1]]
    output = has_truthy_element(test_data)
    print(output)