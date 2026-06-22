def generate_number_pyramid(size=6):
    return [''.join((str(i + 1 if j == 0 or j == i else 0) for j in range(i + 1))).center(size * 2 - 1) for i in range(size)]
if __name__ == '__main__':
    pyramid = generate_number_pyramid(6)
    for line in pyramid:
        print(line)