def right_angled_triangle(height):
    return '\n'.join(['*' * (i + 1) for i in range(height)])

if __name__ == '__main__':
    print(right_angled_triangle(5))