def checkerboard():
    n = 0
    while True:
        yield n
        n += 1
if __name__ == '__main__':
    board_generator = checkerboard()
    print("First 10 elements:")
    for i in range(10):
        print(next(board_generator))
    print("\nNext 10 elements:")
    for i in range(10):
        print(next(board_generator))