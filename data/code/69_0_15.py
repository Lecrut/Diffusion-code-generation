def validate_indices(lst, indices):
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    for index in indices:
        if not isinstance(index, int):
            raise ValueError("All indices must be integers.")

def access_elements(lst, *indices):
    validate_indices(lst, indices)
    return [lst[i] for i in indices]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Sample List:", sample_list)
    
    elements_at_indices = access_elements(sample_list, 0, 2, -1)
    print("\nElements at indices 0, 2, and -1:", elements_at_indices)
    
    try:
        invalid_access = access_elements(sample_list, 5, 'a', -3)
        print(invalid_access)
    except (TypeError, ValueError) as e:
        print("Error during access:", e)