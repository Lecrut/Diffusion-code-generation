def print_square():
    side = 5
    for i in range(side):
        line = ''
        for j in range(side):
            line += '*'
        print(line)

if __name__ == '__main__':
    print_square()