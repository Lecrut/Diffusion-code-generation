POWERS_OF_TWO_COUNT = 10

def generate_powers_of_two(count):
    return [1 << i for i in range(count)]

if __name__ == '__main__':
    powers_of_two = generate_powers_of_two(POWERS_OF_TWO_COUNT)
    print(powers_of_two)