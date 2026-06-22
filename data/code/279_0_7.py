def validate_range(start, end):
    if not (isinstance(start, int) and isinstance(end, int)):
        raise ValueError("Both start and end must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")

def print_numbers():
    start = 0
    end = 10
    validate_range(start, end)
    for i in range(start, end):
        print(i)

if __name__ == '__main__':
    print_numbers()