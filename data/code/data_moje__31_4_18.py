def area_of_square(side_length):
    return side_length * side_length

if __name__ == '__main__':
    sample_sides = [5, 10, 0, 1]
    for side in sample_sides:
        print(area_of_square(side))