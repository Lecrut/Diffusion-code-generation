def odd_even_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield f"{number} is even"
        else:
            yield f"{number} is odd"

if __name__ == '__main__':
    start = 1
    end = 20
    generator = odd_even_generator(start, end)
    for result in generator:
        print(result)