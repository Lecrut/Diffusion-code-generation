def access_elements(lst, *indices):
    def validate_indices(lst, indices):
        valid = True
        for index in indices:
            if not isinstance(index, int) or not (-len(lst) <= index < len(lst)):
                valid = False
                break
        return valid

    if not validate_indices(lst, indices):
        raise IndexError("One or more indices are out of bounds or not integers.")

    result = []
    for index in indices:
        result.append(lst[index])
    
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = (0, -1, 2)
    accessed_elements = access_elements(sample_list, *indices_to_access)
    print(accessed_elements)