if __name__ == '__main__':
    input_data = "10.5\n5.2"
    lines = input_data.strip().split('\n')
    num1 = float(lines[0])
    num2 = float(lines[1])
    result = num1 - num2
    if isinstance(num1, float) and isinstance(num2, float):
        print(f"{result:.2f}")
    else:
        print(result)