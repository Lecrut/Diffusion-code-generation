def odd_even_generator(start, end):
    for number in range(start, end + 1):
        yield (number, "odd" if number % 2 != 0 else "even")

if __name__ == '__main__':
    start_value = 1
    end_value = 20
    for num, result in odd_even_generator(start_value, end_value):
        print(f"{num}: {result}")