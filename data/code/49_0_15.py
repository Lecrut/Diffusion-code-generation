def print_square_star():
    side_length = 5
    for i in range(side_length):
        row = []
        for j in range(side_length):
            row.append('*')
        print(''.join(row))

if __name__ == '__main__':
    print_square_star()