def reverse_range(start, stop):
    if start < stop:
        raise ValueError("Start must be greater than or equal to stop.")
    
    for num in range(start, stop - 1, -1):
        yield num

if __name__ == '__main__':
    try:
        for number in reverse_range(25, 20):
            print(number)
    except ValueError as e:
        print(e)