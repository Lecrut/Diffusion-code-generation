def print_right_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

if __name__ == '__main__':
    sample_values = {5: "right-angled triangle pattern of stars with 5 rows"}
    rows = sample_values[5]
    print_right_triangle(rows)