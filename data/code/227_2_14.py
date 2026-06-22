if __name__ == '__main__':
    rows = 6
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Rows must be a positive integer")
    for i in range(rows, 0, -1):
        print('*' * i)