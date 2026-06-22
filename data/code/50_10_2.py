def print_star_triangle(height):
    if height < 1:
        return
    for i in range(1, height + 1):
        print('*' * i)

if __name__ == '__main__':
    print_star_triangle(5)