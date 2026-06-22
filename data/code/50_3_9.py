def print_star_triangle(rows):
    current_stars = 0
    for _ in range(rows):
        current_stars += 1
        print('*' * current_stars)

if __name__ == '__main__':
    sample_rows = 15
    print_star_triangle(sample_rows)