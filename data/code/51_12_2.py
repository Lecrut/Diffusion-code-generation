def generate_number_pyramid():
    rows = 6
    result = ["".join(str(i - j) for j in range(i + 1)).center(rows * 2 - 1) for i in range(rows)]
    return result

if __name__ == '__main__':
    print(generate_number_pyramid())