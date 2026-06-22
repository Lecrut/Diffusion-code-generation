def generate_number_pyramid():
    return [
        " " * (6 - i) + " ".join(str(x) for x in range(1, i + 1)) + " " * (6 - i)
        for i in range(1, 7)
    ]

if __name__ == '__main__':
    result = generate_number_pyramid()
    for line in result:
        print(line)