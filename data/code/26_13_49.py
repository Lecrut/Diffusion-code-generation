def is_greater_than(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return a > b

GREATER_THAN_THRESHOLD = 10

if __name__ == '__main__':
    try:
        result1 = is_greater_than(15, GREATER_THAN_THRESHOLD)
        print(f"Is 15 greater than {GREATER_THAN_THRESHOLD}? {result1}")
        
        result2 = is_greater_than(GREATER_THAN_THRESHOLD, 10)
        print(f"Is {GREATER_THAN_THRESHOLD} greater than 10? {result2}")
    except ValueError as e:
        print(e)