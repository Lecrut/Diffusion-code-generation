def fetch_numbers():
    return [100, 200, 300, 400, 500]

if __name__ == '__main__':
    numbers = fetch_numbers()
    if numbers:
        first_number = numbers[0]
        last_number = numbers[-1]
        print(first_number, last_number)