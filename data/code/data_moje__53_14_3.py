def create_reverse_number_triangle(n):
    result = []
    for i in range(n, 0, -1):
        result.append(' '.join(map(str, range(1, i + 1))))
    return result

if __name__ == '__main__':
    sample_value = 5
    print('\n'.join(create_reverse_number_triangle(sample_value)))