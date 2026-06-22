def create_reverse_number_triangle(size):
    lines = [" ".join(str(n) for n in range(i, 0, -1)) for i in range(size, 0, -1)]
    return "\n".join(lines)

if __name__ == '__main__':
    sample_size = 5
    result = create_reverse_number_triangle(sample_size)
    print(result)