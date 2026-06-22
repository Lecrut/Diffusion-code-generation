def generate_number_pyramid(rows: int=6) -> list[str]:
    pyramid = []
    for i in range(1, rows + 1):
        row = ''.join((str(j) for j in range(1, i + 1)))
        pyramid.append(row)
    return pyramid
if __name__ == '__main__':
    result = generate_number_pyramid(6)
    for row in result:
        print(row)