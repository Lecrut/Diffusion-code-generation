def validate_input(data):
    if not all(isinstance(item, str) and item.isdigit() for item in data):
        raise ValueError("All elements must be strings representing numbers.")

def find_max_string_numbers(strings):
    validate_input(strings)
    return max(map(int, strings))

if __name__ == '__main__':
    data1 = ["10", "5", "20", "8", "30"]
    print(find_max_string_numbers(data1))
    
    data2 = ["-5", "-1", "-10", "-2"]
    print(find_max_string_numbers(data2))
    
    data3 = ["42"]
    print(find_max_string_numbers(data3))
    
    data4 = []
    try:
        print(find_max_string_numbers(data4))
    except ValueError as e:
        print(e)