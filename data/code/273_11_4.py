def repeat_tasks():
    indices = []
    squares = []

    for i in range(5):
        indices.append(i)
        squares.append(i ** 2)

    print("Indices:", indices)
    print("Squares:", squares)

if __name__ == '__main__':
    repeat_tasks()