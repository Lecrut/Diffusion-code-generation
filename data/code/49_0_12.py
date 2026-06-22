def print_star_square(side_length):
    for i in range(side_length):
        row = ""
        for j in range(side_length):
            row += "*"
        print(row)

if __name__ == '__main__':
    print_star_square(5)