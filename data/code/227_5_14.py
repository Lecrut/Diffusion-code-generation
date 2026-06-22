STARS_PER_LINE = 5

def print_right_angled_triangle():
    for i in range(1, STARS_PER_LINE + 1):
        print('*' * i)

if __name__ == '__main__':
    print_right_angled_triangle()