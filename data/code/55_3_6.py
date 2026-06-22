def inverted_triangle(n):
    result = []
    for i in range(n, 0, -1):
        row = ' '.join(chr(ord('A') + j) for j in range(i))
        result.append(row)
    return result

if __name__ == '__main__':
    sample_size = 5
    print('\n'.join(inverted_triangle(sample_size)))