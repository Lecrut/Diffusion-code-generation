def process_numbers():
    numbers = [10, 23, 45, 56, 67, 89]
    for number in numbers:
        if number > 50:
            break
        if number % 2 == 0:
            continue
        print(number)

if __name__ == '__main__':
    process_numbers()