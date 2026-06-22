def checkerboard_generator(dim):
    if dim <= 0:
        raise ValueError("Dimension must be a positive integer")
    
    def is_even(n):
        return n % 2 == 0
    
    row = [1 if is_even(x) else 0 for x in range(dim)]
    while True:
        yield row
        row = [1 - x for x in row]

if __name__ == '__main__':
    checkerboard = checkerboard_generator(5)
    first_five_rows = [next(checkerboard) for _ in range(5)]
    print(first_five_rows)