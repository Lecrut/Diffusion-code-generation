def is_even(number):
    return number % 2 == 0

def even_numbers():
    for i in range(1, 101):
        if is_even(i):
            yield i

if __name__ == '__main__':
    for number in even_numbers():
        print(number)