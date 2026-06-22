if __name__ == '__main__':
    triangle_height = 5
    result = '\n'.join(' '.join(str(i) for i in range(1, j + 1)) for j in range(1, triangle_height + 1))
    print(result)