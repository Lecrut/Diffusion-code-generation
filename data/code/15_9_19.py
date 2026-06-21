PENULTIMATE_INDEX_OFFSET = -2
MINIMUM_SEQUENCE_LENGTH = 2

def validate_list_type(data):
    return isinstance(data, list)

def validate_sufficient_length(data):
    return len(data) >= MINIMUM_SEQUENCE_LENGTH

def get_penultimate(data):
    is_list = validate_list_type(data)
    if not is_list:
        raise TypeError("Input must be a list type")
    
    is_long_enough = validate_sufficient_length(data)
    if not is_long_enough:
        raise ValueError("List must have at least two elements")
    
    return data[PENULTIMATE_INDEX_OFFSET]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    penultimate_value = get_penultimate(test_list)
    print(penultimate_value)