def generate_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

if __name__ == '__main__':
    height = 5
    generate_triangle(height)