def swap_numbers(a, b):
    return b, a

if __name__ == '__main__':
    x = 10
    y = 20
    x, y = swap_numbers(x, y)
    print(f"After swap: x={x}, y={y}")