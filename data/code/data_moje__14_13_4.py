def get_third_element(seq):
    try:
        return seq[2]
    except IndexError:
        raise ValueError("Sequence must have at least three elements")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (100, 200, 300, 400)
    sample_string = "Hello"

    result_list = get_third_element(sample_list)
    print(result_list)

    result_tuple = get_third_element(sample_tuple)
    print(result_tuple)

    result_string = get_third_element(sample_string)
    print(result_string)