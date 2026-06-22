def is_even_and_zero(num):
    return num % 2 == 0 and num == 0

def even_number_generator(start, end):
    for num in range(start, end + 1):
        if is_even_and_zero(num):
            yield True

if __name__ == '__main__':
    start_value = -5
    end_value = 15
    for result in even_number_generator(start_value, end_value):
        print(result)