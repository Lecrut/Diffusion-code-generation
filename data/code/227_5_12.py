if __name__ == '__main__':
    height = 5
    if not isinstance(height, int) or height < 1:
        raise ValueError("Height must be a positive integer")

    for i in range(1, height + 1):
        print('*' * i)