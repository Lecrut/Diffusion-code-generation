def or_condition(*conditions):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for condition in conditions:
                if condition(result):
                    return True
            return False
        return wrapper
    return decorator

@or_condition(lambda x: x > 0, lambda x: x == 10)
def check_value(x):
    return x
if __name__ == '__main__':
    print(check_value(5))
    print(check_value(-3))
    print(check_value(10))