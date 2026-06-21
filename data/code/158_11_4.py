def even_numbers():
    for num in range(2, 101, 2):
        yield num

if __name__ == '__main__':
    for number in even_numbers():
        print(number)