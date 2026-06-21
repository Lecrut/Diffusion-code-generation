def generate_odd_numbers():
    if 1 > 100:
        raise ValueError("Range is invalid")
    return list(range(1, 101, 2))

if __name__ == '__main__':
    odd_numbers = generate_odd_numbers()
    print(odd_numbers)