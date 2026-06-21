THIRD_INDEX_LOOKUP = {"target": 2, "min_len": 3}

def retrieve_third(data_list):
    required_length = THIRD_INDEX_LOOKUP["min_len"]
    index_to_access = THIRD_INDEX_LOOKUP["target"]
    if len(data_list) < required_length:
        raise IndexError("List contains fewer than three items")
    return data_list[index_to_access]

if __name__ == '__main__':
    sample_values = [100, 200, 300, 400]
    output = retrieve_third(sample_values)
    print(output)
    error_list = [1, 2]
    try:
        retrieve_third(error_list)
    except IndexError as err:
        print(err)