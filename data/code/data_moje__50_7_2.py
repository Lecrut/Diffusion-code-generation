def generate_star_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        result.append("*" * i)
    return "\n".join(result)

if __name__ == '__main__':
    sample_rows = 20
    print(generate_star_triangle(sample_rows))