def generate_star_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        result.append("*" * i)
    return "\n".join(result)

if __name__ == '__main__':
    num_rows = 15
    output = generate_star_triangle(num_rows)
    print(output)