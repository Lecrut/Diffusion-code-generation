ODD = "odd"
EVEN = "even"

def odd_even_generator(start, end):
    for number in range(start, end + 1):
        yield (number, ODD if number % 2 != 0 else EVEN)

if __name__ == '__main__':
    START_VALUE = 1
    END_VALUE = 20
    for num, result in odd_even_generator(START_VALUE, END_VALUE):
        print(f"{num} is {result}")