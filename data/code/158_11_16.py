def is_valid_range(start, end):
    if start < 1 or end > 100:
        raise ValueError("Range must be between 1 and 100 inclusive.")
    if start >= end:
        raise ValueError("Start must be less than end.")

def even_numbers_generator(start, end):
    is_valid_range(start, end)
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

if __name__ == '__main__':
    start = 1
    end = 100
    for number in even_numbers_generator(start, end):
        print(number)