def generate_odd_numbers():
    return list(range(1, 101, 2))

if __name__ == '__main__':
    odd_numbers = generate_odd_numbers()
    for number in odd_numbers:
        print(number)