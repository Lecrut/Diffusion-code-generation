if __name__ == '__main__':
    input_data = [10.5, 5.2]
    num1 = input_data[0]
    num2 = input_data[1]
    result = num1 - num2
    if isinstance(num1, float) or isinstance(num2, float):
        print(f"{result:.2f}")
    else:
        print(result)