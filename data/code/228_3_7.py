MAX_HEIGHT = 10

def generate_right_triangle(height):
    return '\n'.join(' '.join(str(i) for i in range(1, j + 1)) for j in range(1, min(height, MAX_HEIGHT) + 1))

if __name__ == '__main__':
    print(generate_right_triangle(5))