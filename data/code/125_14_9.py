operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}

def perform_operation(operation, num1, num2):
    return operations[operation](num1, num2)

if __name__ == '__main__':
    result_add = perform_operation('add', 5, 3)
    result_subtract = perform_operation('subtract', 7, 4)
    
    assert result_add == 8, "Addition test failed"
    assert result_subtract == 3, "Subtraction test failed"
    
    print(f"Addition of 5 and 3 is: {result_add}")
    print(f"Subtraction of 7 and 4 is: {result_subtract}")