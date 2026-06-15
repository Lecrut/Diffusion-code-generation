def checkerboard_generator():
    n = 0
    while True:
        yield n
        n += 1
if __name__ == '__main__':
    checkerboard = checkerboard_generator()
    first_ten = [next(checkerboard) for _ in range(10)]
    print(first_ten)