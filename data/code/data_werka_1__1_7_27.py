def validate_weight(func):

    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError('Weight must be an integer or float.')
        if weight < 0:
            raise ValueError('Weight cannot be negative.')
        return func(weight)
    return wrapper

@validate_weight
def process_weight(weight):
    return f'Processed weight: {weight}'
if __name__ == '__main__':
    try:
        print(process_weight(75))
        print(process_weight(-10))
    except Exception as e:
        print(e)
    try:
        print(process_weight('100'))
    except Exception as e:
        print(e)