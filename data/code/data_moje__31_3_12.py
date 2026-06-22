def get_square_area(side):
    return float(side) * float(side)

if __name__ == '__main__':
    side_values = [4.5, 0.003, 12.125]
    for value in side_values:
        print(get_square_area(value))