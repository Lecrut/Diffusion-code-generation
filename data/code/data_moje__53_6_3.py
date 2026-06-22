def reverse_number_triangle(height):
    result = []
    current = height * (height + 1) // 2
    for _ in range(height):
        row_numbers = []
        for _ in range(height):
            row_numbers.append(str(current))
            current -= 1
        result.append(" ".join(row_numbers))
    return "\n".join(result)

if __name__ == '__main__':
    print(reverse_number_triangle(4))