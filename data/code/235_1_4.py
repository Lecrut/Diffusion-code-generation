def print_square_box(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    
    for _ in range(size):
        print('#' * size)

if __name__ == '__main__':
    try:
        print_square_box(4)
    except Exception as e:
        print(e)