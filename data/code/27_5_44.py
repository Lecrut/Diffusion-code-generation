def check_not_equal(threshold):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f'Result is equal to the threshold value: {threshold}')
            return result
        return wrapper
    return decorator

@check_not_equal(0)
def difference(a, b):
    return a - b

if __name__ == '__main__':
    try:
        value1 = 15
        value2 = 7
        print(f"Difference between {value1} and {value2}: {difference(value1, value2)}")
        
        value3 = 9
        value4 = 9
        print(f"Difference between {value3} and {value4}: {difference(value3, value4)}")
    except ValueError as e:
        print(e)