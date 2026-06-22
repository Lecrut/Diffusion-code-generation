def ounces_to_grams(ounces):
    if not isinstance(ounces, (int, float)):
        raise ValueError('Input must be a number')
    return int(ounces * 28.3495)
if __name__ == '__main__':
    print(ounces_to_grams(1))
    print(ounces_to_grams(0.5))