def generate_reverse_triangle():
    return '\n'.join(' '.join(str(j) for j in range(i, 0, -1)) for i in range(5, 0, -1))

if __name__ == '__main__':
    print(generate_reverse_triangle())