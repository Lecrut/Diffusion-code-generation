def print_triangle(height):
    for i in range(1, height + 1):
        print("*" * i)

if __name__ == '__main__':
    height = 5
    result = print_triangle(height)
    print(result)