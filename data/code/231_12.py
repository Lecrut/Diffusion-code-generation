def generate_triangle(height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
if __name__ == '__main__':
    triangle_height = 5
    generate_triangle(triangle_height)