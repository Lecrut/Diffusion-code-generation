def capitalize_decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise ValueError('The decorated function must return a string.')
        words = result.split()
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)
    return wrapper

@capitalize_decorator
def get_greeting(name):
    return f'hello {name}'
if __name__ == '__main__':
    sample_name = 'world'
    try:
        greeting = get_greeting(sample_name)
        print('Greeting:', greeting)
    except ValueError as e:
        print('Error:', e)
    invalid_input = 12345
    try:
        result = get_greeting(invalid_input)
    except ValueError as e:
        print('Error with invalid input:', e)