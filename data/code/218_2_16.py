def find_min_value(float_list):
    if not float_list:
        raise ValueError("List is empty")
    
    min_value = float_list[0]
    for value in float_list[1:]:
        if value < min_value:
            min_value = value
    
    return min_value

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9, 2.7]
    print(find_min_value(sample_values))