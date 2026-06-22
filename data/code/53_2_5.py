def generate_reverse_triangle(height: int) -> list[str]:
    result = []
    for i in range(height, 0, -1):
        row = " ".join(str(n) for n in range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    lines = generate_reverse_triangle(6)
    for line in lines:
        print(line)