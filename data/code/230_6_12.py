def reverse_range(start, end):
    if start >= end:
        raise ValueError("Start must be less than end")
    
    for i in range(end - 1, start - 1, -1):
        yield i

if __name__ == '__main__':
    try:
        for number in reverse_range(5, 0):
            print(number)
    except ValueError as e:
        print(e)