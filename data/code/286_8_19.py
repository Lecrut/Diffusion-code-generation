def is_valid_km(value: float) -> bool:
    return isinstance(value, (int, float)) and value >= 0

def km_to_miles(km: float) -> float:
    if not is_valid_km(km):
        raise ValueError(f'Invalid kilometers provided: {km}. Must be a non-negative number.')
    return km * 0.621371
if __name__ == '__main__':
    test_cases = [(10.0,), (5.0,), (0.0,), (-1.0,), ('five',)]
    for km in test_cases:
        try:
            miles = km_to_miles(km[0])
            print(f'{km[0]} kilometers is {miles} miles.')
        except ValueError as e:
            print(e)