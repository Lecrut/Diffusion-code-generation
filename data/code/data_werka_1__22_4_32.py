def odd_even_generator(start, end):
    for num in range(start, end + 1):
        yield (num, "Odd" if num % 2 != 0 else "Even")

if __name__ == '__main__':
    start = 1
    end = 20
    for number, result in odd_even_generator(start, end):
        print(f"{number}: {result}")