def checkerboard_generator(dim):
    if not isinstance(dim, int) or dim <= 0:
        raise ValueError("Dimension must be a positive integer")
    
    for i in range(dim):
        row = [1 if (i + j) % 2 == 0 else 0 for j in range(dim)]
        yield row

if __name__ == '__main__':
    checkerboard = checkerboard_generator(5)
    print(next(checkerboard))
    print(next(checkerboard))