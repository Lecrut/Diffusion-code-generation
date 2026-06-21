def convert_to_floats(data_list):
    if not all(isinstance(item, (int, float)) for item in data_list):
        raise ValueError("All elements must be integers or floats")
    return [float(item) for item in data_list]

def get_maximum(data_list):
    float_list = convert_to_floats(data_list)
    return max(float_list)

if __name__ == '__main__':
    sample_data1 = [10, 5, 20, 8, 15]
    sample_data2 = [-5, -1, -10, -3]
    sample_data3 = [42.5, 42.6, 42.7]
    
    print(f"Maximum of {sample_data1}: {get_maximum(sample_data1)}")
    print(f"Maximum of {sample_data2}: {get_maximum(sample_data2)}")
    print(f"Maximum of {sample_data3}: {get_maximum(sample_data3)}")