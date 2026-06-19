def extract_every_second_element(data_list):
    try:
        if not isinstance(data_list, list):
            raise TypeError("Input must be a list.")
        return [data_list[i] for i in range(len(data_list)) if i % 2 == 0]
    except TypeError as e:
        print(e)
        return []

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70]
    result = extract_every_second_element(sample_list)
    print("Extracted elements:", result)

    invalid_input = "not a list"
    result_invalid = extract_every_second_element(invalid_input)
    print("Result with invalid input:", result_invalid)