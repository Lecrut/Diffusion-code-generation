def status_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield 'Even'
        else:
            yield 'Odd'
if __name__ == '__main__':
    generator = status_generator(1, 20)
    for status in generator:
        print(status)