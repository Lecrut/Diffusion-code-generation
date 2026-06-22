checkerboard = [[(i + j) % 2 for i in range(10)] for j in range(10)]

if __name__ == '__main__':
    print("Checkerboard:")
    for row in checkerboard:
        print(row)