ODD_NUMBER_GENERATOR = range(1, 101, 2)

def generate_odd_numbers():
    return list(ODD_NUMBER_GENERATOR)

if __name__ == '__main__':
    odd_numbers = generate_odd_numbers()
    print(odd_numbers)