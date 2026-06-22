def determine_the_largest_number_present_compare():
    sample_values = {
        'list1': [3.14, 1.618, 2.718, 0.577],
        'list2': [-10.5, -5.2, -20.1, -1.0],
        'list3': [42.0]
    }
    
    max_values = {key: max(values) for key, values in sample_values.items()}
    
    return max_values

if __name__ == '__main__':
    result = determine_the_largest_number_present_compare()
    print(result)