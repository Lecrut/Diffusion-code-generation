def validate_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end must be integers.")
    if start > end:
        raise ValueError("Start must be less than or equal to end.")

def is_zero(num):
    return num == 0

def even_number_generator(start, end):
    validate_range(start, end)
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield is_zero(num)

if __name__ == '__main__':
    start_value = -3
    end_value = 7
    for result in even_number_generator(start_value, end_value):
        print(result)