def odd_even_generator(start, end):
    for number in range(start, end + 1):
        yield (number, "Odd" if number % 2 != 0 else "Even")

if __name__ == '__main__':
    start = 1
    end = 20
    for num, result in odd_even_generator(start, end):
        print(f"{num}: {result}")