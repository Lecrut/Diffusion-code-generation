def multiply_variables(a, b):
    return a * b
if __name__ == '__main__':
    variable1 = 15
    variable2 = 7
    if isinstance(variable1, (int, float)) and isinstance(variable2, (int, float)):
        result = multiply_variables(variable1, variable2)
        print(result)
    else:
        print("Error: Both inputs must be valid numbers.")