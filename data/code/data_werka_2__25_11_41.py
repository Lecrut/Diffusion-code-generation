def is_even(num):
    return num % 2 == 0

def even_zero_generator(start, end):
    for num in range(start, end + 1):
        if is_even(num):
            yield num == 0

if __name__ == '__main__':
    start_value = -3
    end_value = 7
    for result in even_zero_generator(start_value, end_value):
        print(result)