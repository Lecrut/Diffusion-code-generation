def even_zero_generator(start, end):
    if start > end:
        raise ValueError("Start value cannot be greater than end value.")
    
    def is_even(num):
        return num % 2 == 0
    
    for num in range(start, end + 1):
        if is_even(num):
            yield num == 0

if __name__ == '__main__':
    start = -3
    end = 7
    try:
        for result in even_zero_generator(start, end):
            print(result)
    except ValueError as e:
        print(e)