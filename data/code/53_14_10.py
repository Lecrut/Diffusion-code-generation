def print_reverse_triangle(n: int) -> None:
    for i in range(n, 0, -1):
        print('* ' * i)

if __name__ == '__main__':
    sample_value = 5
    print_reverse_triangle(sample_value)