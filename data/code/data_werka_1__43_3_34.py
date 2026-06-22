if __name__ == '__main__':
    side_length = 6
    area_of_square = lambda s: s ** 2 if s > 0 else None
    print(area_of_square(side_length))