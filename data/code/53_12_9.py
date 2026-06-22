def construct_reverse_number_triangle(n):
    return ["".join(str(x) for x in range(i, 0, -1)) for i in range(n, 0, -1)]

if __name__ == '__main__':
    sample_size = 5
    result = construct_reverse_number_triangle(sample_size)
    for line in result:
        print(line)