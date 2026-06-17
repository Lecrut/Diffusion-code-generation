def find_largest_value(numbers: list[float]) -> float | None:
    max_val = float('-inf')
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Expected numeric value but got {type(item).__name__}")
        if item > max_val:
            max_val = float(item)
    return max_val
if __name__ == '__main__':
    test_data_1 = [3.5, 7.2, -4.0, 9.8]
    test_data_2 = []
    test_data_3 = [-100, -50, -1]
    print(f"Largest in {test_data_1}: ", find_largest_value(test_data_1))                 
    print("Largest in empty list:", find_largest_value(test_data_2))                   
    try:
        result = find_largest_value(test_data_3)
        print(f"Largest in {test_data_3}: ", result)                  
    except Exception as e:
        print("An error occurred:", type(e).__name__)