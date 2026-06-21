def generate_odd_numbers():
    odd_numbers = list(range(1, 101, 2))
    return odd_numbers

if __name__ == '__main__':
    odd_numbers = generate_odd_numbers()
    print(odd_numbers)