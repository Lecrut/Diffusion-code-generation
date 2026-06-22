def print_star_square(size=5):
    for i in range(size):
        line = ""
        for j in range(size):
            line += "*"
        print(line)

if __name__ == '__main__':
    print_star_square(5)