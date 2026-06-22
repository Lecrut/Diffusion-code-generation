def validate_ounces(value):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError('Ounces must be a non-negative number')

def ounces_to_grams(ounces):
    validate_ounces(ounces)
    return int(ounces * 28.3495)
if __name__ == '__main__':
    print(ounces_to_grams(1))
    print(ounces_to_grams(0.5))
    print(ounces_to_grams(10))