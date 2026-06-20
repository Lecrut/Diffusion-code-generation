def divide_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    
    result = []
    for num1, num2 in zip(list1, list2):
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        result.append(num1 / num2)
    
    return result

if __name__ == '__main__':
    sample_list1 = [10, 15, 7]
    sample_list2 = [2, 3, 0]
    try:
        print(divide_elements(sample_list1, sample_list2))
    except ValueError as err:
        print(f"Error caught: {err}")