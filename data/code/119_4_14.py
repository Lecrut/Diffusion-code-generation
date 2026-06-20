def swap_numbers(x, y):
    temp = x
    x = y
    y = temp
    return (x, y)

if __name__ == '__main__':
    num1, num2 = 7, 8
    swapped_nums = swap_numbers(num1, num2)
    print(swapped_nums)