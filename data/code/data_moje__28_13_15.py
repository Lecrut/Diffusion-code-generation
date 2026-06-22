def sort_two_numbers(a, b):
    if a < b:
        return a, b
    return b, a

if __name__ == '__main__':
    first = 42
    second = 17
    sorted_first, sorted_second = sort_two_numbers(first, second)
    print(sorted_first, sorted_second)
    x = -5
    y = -5
    sorted_x, sorted_y = sort_two_numbers(x, y)
    print(sorted_x, sorted_y)
    num1 = 100
    num2 = 0.5
    sorted_num1, sorted_num2 = sort_two_numbers(num1, num2)
    print(sorted_num1, sorted_num2)