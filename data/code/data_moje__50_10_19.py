def print_right_angled_triangle(height):
    if height < 0:
        return
    for i in range(1, height + 1):
        print('*' * i)

if __name__ == '__main__':
    sample_height = 5
    print_right_angled_triangle(sample_height)