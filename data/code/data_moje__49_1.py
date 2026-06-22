def print_star_square(size):
    if size <= 0:
        return
    if size == 1:
        print("*")
        return
    
    print("*" * size)
    for _ in range(size - 2):
        print("*" + " " * (size - 2) + "*")
    print("*" * size)

if __name__ == '__main__':
    print_star_square(1)
    print()
    print_star_square(5)
    print()
    print_star_square(10)