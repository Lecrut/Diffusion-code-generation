def convert_km_to_m(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number")
    if kilometers < 0:
        raise ValueError("Input must be a non-negative number")
    return kilometers * 1000

if __name__ == '__main__':
    sample_value_1 = 5
    sample_value_2 = 2.5
    sample_value_3 = -1
    
    print(convert_km_to_m(sample_value_1))
    print(convert_km_to_m(sample_value_2))
    try:
        print(convert_km_to_m(sample_value_3))
    except ValueError as e:
        print(f"Error: {e}")