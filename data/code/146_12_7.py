def process_numbers():
    numbers = [10, 23, 45, 56, 67, 89]
    for num in numbers:
        if num > 50:
            break
        if num % 2 == 0:
            continue
        print(num)

if __name__ == '__main__':
    process_numbers()