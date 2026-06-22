def median_of_three(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    num1 = 5
    num2 = 2
    num3 = 8
    result = median_of_three(num1, num2, num3)
    print(result)