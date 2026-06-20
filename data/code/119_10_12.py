def swap_values(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return b, a

if __name__ == '__main__':
    x, y = 5, 10
    try:
        x, y = swap_values(x, y)
        print(f"Swapped values: x={x}, y={y}")
    except ValueError as e:
        print(e)