def find_the_middle_value_among_three_transform(a, b, c):
    max_val = max(a, b, c)
    min_val = min(a, b, c)
    middle_val = (a + b + c) - max_val - min_val
    return middle_val

if __name__ == '__main__':
    num1 = 7
    num2 = 3
    num3 = 5
    median = find_the_middle_value_among_three_transform(num1, num2, num3)
    print(median)