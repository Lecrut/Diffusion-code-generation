def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == '__main__':
    test_cases = {
        (2, 3): {"addition": 5, "subtraction": -1},
        (5, 2): {"addition": 7, "subtraction": 3}
    }
    
    for inputs, expected in test_cases.items():
        num1, num2 = inputs
        addition_result = add(num1, num2)
        subtraction_result = subtract(num1, num2)
        
        assert addition_result == expected["addition"], f"Addition test failed for {inputs}"
        assert subtraction_result == expected["subtraction"], f"Subtraction test failed for {inputs}"
        
        print(f"Addition of {num1} and {num2} is: {addition_result}")
        print(f"Subtraction of {num1} and {num2} is: {subtraction_result}")