def access_elements(lst, *indices):
    def validate_indices(lst, indices):
        valid_indices = []
        for index in indices:
            if isinstance(index, int) and -len(lst) <= index < len(lst):
                valid_indices.append(index)
            else:
                raise ValueError(f"Invalid index: {index}")
        return valid_indices

    valid_indices = validate_indices(lst, indices)
    return [lst[i] for i in valid_indices]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = (0, 2, -1, 5)
    try:
        result = access_elements(sample_list, *indices_to_access)
        print(result)
    except ValueError as e:
        print(e)