def validate_range(start, end):
    if start < 1 or end > 10:
        raise ValueError("Start and end must be between 1 and 10")

def cycle_range():
    for i in range(1, 11):
        print(i)

if __name__ == '__main__':
    validate_range(1, 10)
    cycle_range()