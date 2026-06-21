def even_numbers():
    for i in range(2, 101, 2):
        yield i

if __name__ == '__main__':
    generator = even_numbers()
    for number in generator:
        print(number)