def generate_number_pyramid(size):
    return [''.join([str(i + 1) for i in range(j + 1)]) for j in range(size)]
if __name__ == '__main__':
    pyramid = generate_number_pyramid(6)
    for line in pyramid:
        print(line)