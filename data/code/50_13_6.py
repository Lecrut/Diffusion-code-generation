def inverted_right_angled_triangle(size):
    result = []
    for i in range(size, 0, -1):
        result.append('*' * i)
    return '\n'.join(result)

if __name__ == '__main__':
    print(inverted_right_angled_triangle(5))