def generate_number_pyramid():
    n = 6
    return [str(i) for j in range(1, n + 1) for i in range(1, j + 1)]

if __name__ == '__main__':
    print(generate_number_pyramid())