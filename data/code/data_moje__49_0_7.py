def print_square_star_pattern(side_length):
    for i in range(side_length):
        line = ""
        for j in range(side_length):
            line += "*"
        print(line)

if __name__ == '__main__':
    print_square_star_pattern(5)