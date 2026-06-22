def get_larger_value_in_original_unit(value1_meters, value2_meters):
    value1_cm = value1_meters * 100
    value2_cm = value2_meters * 100
    
    if value1_cm >= value2_cm:
        return value1_meters
    else:
        return value2_meters

if __name__ == '__main__':
    result = get_larger_value_in_original_unit(5.5, 3.2)
    print(result)