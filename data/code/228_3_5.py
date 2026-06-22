if __name__ == '__main__':
    height = 5
    triangle = '\n'.join(' '.join(str(i) for i in range(1, j + 1)) for j in range(1, height + 1))
    print(triangle)