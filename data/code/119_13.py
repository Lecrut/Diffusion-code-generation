def swap_numbers(a, b):
    a, b = b, a
if __name__ == '__main__':
    x = 10
    y = 20
    print(f"Before swap: x={x}, y={y}")
    swap_numbers(x, y)
    print(f"After swap: x={x}, y={y}")