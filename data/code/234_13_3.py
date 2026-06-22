if __name__ == '__main__':
    checkerboard = [[(i + j) % 2 for j in range(10)] for i in range(10)]
    print(checkerboard)