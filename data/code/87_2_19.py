POSITIVE_THRESHOLD = 0
MAX_VALUE = 100

def is_positive_and_less_than_100(value: int) -> bool:
    return value > POSITIVE_THRESHOLD and value < MAX_VALUE

if __name__ == '__main__':
    result1 = is_positive_and_less_than_100(50)
    print(f"is_positive_and_less_than_100(50) is: {result1}")
    
    result2 = is_positive_and_less_than_100(-10)
    print(f"is_positive_and_less_than_100(-10) is: {result2}")
    
    result3 = is_positive_and_less_than_100(100)
    print(f"is_positive_and_less_than_100(100) is: {result3}")
    
    result4 = is_positive_and_less_than_100(0)
    print(f"is_positive_and_less_than_100(0) is: {result4}")