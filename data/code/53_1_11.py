def generate_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        numbers = ''.join(str(j) for j in range(i, 0, -1))
        padded = numbers.rjust(rows * 2 - 1)
        result.append(padded)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_reverse_number_triangle(4))