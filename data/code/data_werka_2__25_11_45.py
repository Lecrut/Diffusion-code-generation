def is_even(num):
    return num % 2 == 0

def even_zero_generator(start, end):
    for num in range(start, end + 1):
        if is_even(num):
            yield num == 0

if __name__ == '__main__':
    start = -3
    end = 7
    for result in even_zero_generator(start, end):
        print(result)