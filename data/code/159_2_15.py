MAX_NUMBER = 100

def generate_odd_numbers():
    return list(range(1, MAX_NUMBER + 1, 2))

if __name__ == '__main__':
    odd_numbers = generate_odd_numbers()
    print(odd_numbers)