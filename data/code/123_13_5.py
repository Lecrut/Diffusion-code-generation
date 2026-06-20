def calculate_sum(start, end):
    if not (isinstance(start, int) and isinstance(end, int)):
        raise ValueError("Both start and end must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    return sum(x for x in range(start, end + 1))

if __name__ == '__main__':
    result = calculate_sum(1, 100)
    print(result)