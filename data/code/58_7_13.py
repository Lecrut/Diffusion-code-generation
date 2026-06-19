def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    return data

def get_first_element(data):
    validated_data = validate_input(data)
    if not validated_data:
        return None
    return validated_data[0]

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4]
    sample2 = ['x', 'y', 'z']
    empty_list = []
    single_item = [999]
    
    print(f"First element of {sample1}: {get_first_element(sample1)}")
    print(f"First element of {sample2}: {get_first_element(sample2)}")
    print(f"First element of {empty_list}: {get_first_element(empty_list)}")
    print(f"First element of {single_item}: {get_first_element(single_item)}")