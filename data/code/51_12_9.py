def create_number_pyramid(size=6):
    return [
        " ".join(str(j) for j in range(1, i + 1)).center(size * 4)
        for i in range(1, size + 1)
    ]

if __name__ == '__main__':
    result = create_number_pyramid(6)
    for line in result:
        print(line)