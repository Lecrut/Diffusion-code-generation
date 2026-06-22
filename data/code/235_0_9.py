MAX_HEIGHT = 5

def generate_right_angled_triangle(height):
    if height > MAX_HEIGHT:
        raise ValueError("Height exceeds maximum allowed value")

    for i in range(1, height + 1):
        print('*' * i)

if __name__ == '__main__':
    try:
        triangle_height = 5
        generate_right_angled_triangle(triangle_height)
    except ValueError as e:
        print(e)