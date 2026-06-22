CONSTANT_VALUE = 42

def match_checker(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == CONSTANT_VALUE:
            return 'Match found!'
        else:
            return f'No match. Expected {CONSTANT_VALUE}, got {result}'
    return wrapper

@match_checker
def sample_function(x):
    return x * 7
if __name__ == '__main__':
    print(sample_function(6))
    print(sample_function(5))