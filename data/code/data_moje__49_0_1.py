def print_square():
    side_length = 5
    for i in range(side_length):
        for j in range(side_length):
            if j == side_length - 1:
                print("*", end="")
            else:
                print("*", end=" ")
        print()

if __name__ == '__main__':
    print_square()