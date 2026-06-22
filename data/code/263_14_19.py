def find_largest_of_three(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

if __name__ == '__main__':
    num1 = 3.5
    num2 = 7.2
    num3 = 5.8
    largest_number = find_largest_of_three(num1, num2, num3)
    print(f"The largest number among {num1}, {num2}, and {num3} is {largest_number}")