def generate_number_pyramid(size=6):
    return [''.join((str(i + 1) for _ in range(1, i + 2))) for i in range(size)]
if __name__ == '__main__':
    pyramid = generate_number_pyramid()
    for line in pyramid:
        print(line)