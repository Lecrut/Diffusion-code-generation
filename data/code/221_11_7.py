def order_three(a, b, c):
    numbers = [a, b, c]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return tuple(numbers)

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    num3 = 1
    result = order_three(num1, num2, num3)
    print(result)