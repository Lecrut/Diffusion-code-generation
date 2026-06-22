def median_of_three(a, b, c):
    x = (a + b) // 2
    y = (b + c) // 2
    z = (c + a) // 2
    return max(min(x, y), min(max(x, y), z))

if __name__ == '__main__':
    num1 = 5
    num2 = 2
    num3 = 8
    median_result = median_of_three(num1, num2, num3)
    print(median_result)