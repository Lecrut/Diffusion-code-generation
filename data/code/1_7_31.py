def validate_and_normalize_weight(func):

    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError('Weight must be a number.')
        if weight < 0:
            raise ValueError('Weight cannot be negative.')
        if weight >= 2.20462:
            weight /= 2.20462
        return func(weight)
    return wrapper

@validate_and_normalize_weight
def process_weight(weight):
    return f'Processed weight: {weight} kg'
if __name__ == '__main__':
    try:
        print(process_weight(150))
        print(process_weight(-5))
        print(process_weight('100'))
    except Exception as e:
        print(e)