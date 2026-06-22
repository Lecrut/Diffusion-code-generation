def construct_reverse_number_triangle(n):
    lines = [
        ' '.join(str(i) for i in range(1, n - row + 1))
        for row in range(n)
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_size = 5
    result = construct_reverse_number_triangle(sample_size)
    print(result)