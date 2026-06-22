def determine_the_largest_number_present_compare():
    sample_value_1 = 42
    sample_value_2 = 99
    
    if sample_value_1 > sample_value_2:
        return {'largest': sample_value_1}
    else:
        return {'largest': sample_value_2}

if __name__ == '__main__':
    result = determine_the_largest_number_present_compare()
    print(result)