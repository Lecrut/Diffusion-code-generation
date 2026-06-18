def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    numbers = [10, 5]
    index = 0
    while True:
        if index >= len(numbers):
            break
        num1 = numbers[index]
        num2 = numbers[index + 1]
        result = calculate_difference(num1, num2)
        print(f"Result: {result}")
        index += 2
    print("exit")