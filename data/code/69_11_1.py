def access_list_elements(data, indices):
    result = []
    for index in indices:
        if 0 <= index < len(data):
            result.append(data[index])
        else:
            result.append(None)
    return result
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices_valid = [0, 2, 4]
    sample_indices_invalid = [1, 5, -1, 3]
    result_valid = access_list_elements(sample_list, sample_indices_valid)
    print(f"Sample List: {sample_list}")
    print(f"Sample Indices (Valid): {sample_indices_valid}")
    print(f"Result (Valid Indices): {result_valid}")
    result_invalid = access_list_elements(sample_list, sample_indices_invalid)
    print(f"Sample Indices (Invalid): {sample_indices_invalid}")
    print(f"Result (Invalid Indices): {result_invalid}")