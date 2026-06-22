def check_truth(condition):

    def decorator(func):

        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                return None
        return wrapper
    return decorator

@check_truth(True)
def greet(name):
    return f'Hello, {name}!'

@check_truth(False)
def farewell(name):
    return f'Goodbye, {name}!'
if __name__ == '__main__':
    print(greet('Alice'))
    print(farewell('Bob'))