def print_solid_pyramid():
    for row in range(1, 6):
        print(" " * (5 - row) + str(row) * row)

if __name__ == '__main__':
    print_solid_pyramid()