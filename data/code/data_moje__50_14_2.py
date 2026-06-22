def print_diamond(n):
    upper_height = n
    lower_height = n - 1

    for i in range(upper_height):
        spaces = " " * (upper_height - 1 - i)
        stars = "* " * (i + 1)
        print(spaces + stars.rstrip())

    for i in range(lower_height):
        spaces = " " * (i + 1)
        stars = "* " * (lower_height - i)
        print(spaces + stars.rstrip())

if __name__ == '__main__':
    sample_height = 5
    print_diamond(sample_height)