def multiply(a: float, b: float) -> float:
    return a * b
if __name__ == '__main__':
    value1 = 3.141592653589793
    value2 = 2.718281828459045
    intermediate_result = multiply(value1, value2)
    final_result = round(intermediate_result, 50)
    print(final_result)