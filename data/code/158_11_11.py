def is_valid_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers")
    if start < 1 or end > 100:
        raise ValueError("Start must be between 1 and 100, inclusive; End must be between 1 and 100, inclusive")

def even_numbers(start=1, end=100):
    is_valid_range(start, end)
    for num in range(max(2, start), end + 1, 2):
        yield num

if __name__ == '__main__':
    for number in even_numbers():
        print(number)