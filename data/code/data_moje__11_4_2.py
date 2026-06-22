def retrieve_final_element(data):
    if len(data) == 0:
        raise IndexError("Cannot retrieve element from an empty list")
    final_index = len(data) - 1
    return data[final_index]

if __name__ == '__main__':
    test_collection = ["alpha", "beta", "gamma", "delta", "epsilon"]
    result = retrieve_final_element(test_collection)
    print(result)