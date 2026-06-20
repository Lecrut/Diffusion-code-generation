def is_greater_than_ten(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    return num > 10

if __name__ == '__main__':
    sample_value_1 = 5
    sample_value_2 = 15
    
    result_1 = is_greater_than_ten(sample_value_1)
    print(f"Is {sample_value_1} greater than ten? {result_1}")
    
    result_2 = is_greater_than_ten(sample_value_2)
    print(f"Is {sample_value_2} greater than ten? {result_2}")