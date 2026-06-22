def mph_to_kmh(mph):
    conversion_factor = 1.60934
    if not isinstance(mph, (int, float)):
        raise ValueError('Input must be a number.')
    return f'{mph * conversion_factor:.2f} km/h'
if __name__ == '__main__':
    print(mph_to_kmh(50))