def abs_diff(y1, y2):
    return abs(y1 - y2)

if __name__ == '__main__':
    year_a = 2023
    year_b = 1985
    difference = abs_diff(year_a, year_b)
    print(difference)