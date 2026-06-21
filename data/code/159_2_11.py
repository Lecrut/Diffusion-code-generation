def generate_odd_numbers():
    odd_numbers = list(range(1, 101, 2))
    return odd_numbers

if __name__ == '__main__':
    result = generate_odd_numbers()
    print("Odd numbers between 1 and 100:", result)