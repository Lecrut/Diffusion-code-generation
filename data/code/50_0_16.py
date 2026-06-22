def print_right_aligned_triangle():
    for i in range(1, 11):
        print(' ' * (10 - i) + '*' * i)

if __name__ == '__main__':
    print_right_aligned_triangle()