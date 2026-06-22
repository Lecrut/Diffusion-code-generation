units = {'cm': 1, 'm': 100}

def compare_lengths(length1: float, unit1: str, length2: float, unit2: str) -> str:
    length1_cm = length1 * units[unit1]
    length2_cm = length2 * units[unit2]
    if length1_cm < length2_cm:
        return f'{length1} {unit1}'
    else:
        return f'{length2} {unit2}'
if __name__ == '__main__':
    print(compare_lengths(50, 'cm', 3, 'm'))
    print(compare_lengths(2.5, 'm', 250, 'cm'))