def kg_to_lbs(kilograms):
    if not isinstance(kilograms, (int, float)):
        raise ValueError('Input must be a number.')
    return kilograms * 2.20462
if __name__ == '__main__':
    print(kg_to_lbs(1))
    print(kg_to_lbs(2.5))
    print(kg_to_lbs(0))