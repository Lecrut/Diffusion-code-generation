def process_numbers():
    numbers = [3, 5, 8, 10, 23, 45, 60, 70]
    for number in numbers:
        if number > 50:
            break
        if number % 2 == 0:
            continue
        print(number)

if __name__ == '__main__':
    process_numbers()