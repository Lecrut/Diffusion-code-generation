SWAP_LIST = [None]

def swap_values(a, b):
    SWAP_LIST[0] = a
    a = b
    b = SWAP_LIST[0]
    return a, b

if __name__ == '__main__':
    x, y = 5, 10
    swapped_x, swapped_y = swap_values(x, y)
    print(f"Swapped values: x={swapped_x}, y={swapped_y}")