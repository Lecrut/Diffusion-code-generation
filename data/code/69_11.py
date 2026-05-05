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
    result1 = access_list_elements(sample_list, sample_indices_valid)
    print(f"List: {sample_list}")
    print(f"Indices: {sample_indices_valid}")
    print(f"Result 1: {result1}")
    result2 = access_list_elements(sample_list, sample_indices_invalid)
    print(f"List: {sample_list}")
    print(f"Indices: {sample_indices_invalid}")
    print(f"Result 2: {result2}")