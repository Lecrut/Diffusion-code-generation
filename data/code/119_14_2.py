def reverse_numbers(x, y):
    temp = x
    x = y
    y = temp
    return (x, y)

if __name__ == '__main__':
    print(reverse_numbers(10, 20))