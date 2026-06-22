def generate_number_pyramid() -> str:
    rows = [str(i) for i in range(1, 4)]
    max_width = len(rows[-1])
    result = []
    for row in rows:
        padded = row.center(max_width)
        result.append(padded)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_number_pyramid())