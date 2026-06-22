def validate_weight(func):

    def wrapper(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError('Weight must be a number.')
        if weight < 0:
            raise ValueError('Weight cannot be negative.')
        return func(weight)
    return wrapper

@validate_weight
def process_weight(weight):
    if weight >= 2.20462:
        normalized_weight = weight / 2.20462
        return f'Normalized Weight: {normalized_weight:.2f} kg'
    else:
        return f'Weight: {weight} kg'
if __name__ == '__main__':
    sample_weights = [70, -5, '100', 230.45]
    for weight in sample_weights:
        try:
            print(process_weight(weight))
        except (TypeError, ValueError) as e:
            print(e)