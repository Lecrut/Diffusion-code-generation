def inverted_triangle_star_pattern(rows):
    for i in range(rows, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    inverted_triangle_star_pattern(6)