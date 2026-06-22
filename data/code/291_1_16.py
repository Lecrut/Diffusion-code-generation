def validate_length_and_unit(length: float, unit: str) -> None:
    if not isinstance(length, (int, float)) or length < 0:
        raise ValueError('Length must be a non-negative number.')
    if unit != 'cm':
        raise ValueError("Unit must be 'cm'.")

def get_shorter_length(length1: float, unit1: str, length2: float, unit2: str) -> str:
    validate_length_and_unit(length1, unit1)
    validate_length_and_unit(length2, unit2)
    if unit1 == 'cm' and unit2 == 'cm':
        return f'{min(length1, length2)} cm'
    else:
        raise ValueError('Unsupported units for comparison.')
if __name__ == '__main__':
    print(get_shorter_length(50, 'cm', 75, 'cm'))
    print(get_shorter_length(3, 'm', 2.5, 'm'))