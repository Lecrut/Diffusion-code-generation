def checkerboard_generator():
    n = 0
    while True:
        yield n
        n += 1
if __name__ == '__main__':
    checkerboard = checkerboard_generator()
    print("First 10 elements:")
    for i in range(10):
        print(next(checkerboard))
    print("\nNext 10 elements:")
    for i in range(10):
        print(next(checkerboard))