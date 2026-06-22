def print_square(size):
    return ("\n".join(["*" * size] * size) + "\n")

if __name__ == '__main__':
    print(print_square(7))