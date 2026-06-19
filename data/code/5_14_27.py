import math

def normalize_and_compare(length1, unit1, length2, unit2):
    inches_to_cm = 2.54
    if unit1 == 'inches':
        length1_cm = length1 * inches_to_cm
    else:
        length1_cm = length1
    if unit2 == 'inches':
        length2_cm = length2 * inches_to_cm
    else:
        length2_cm = length2
    if length1_cm > length2_cm:
        return f'{length1} {unit1} is greater than {length2} {unit2}'
    elif length1_cm < length2_cm:
        return f'{length1} {unit1} is less than {length2} {unit2}'
    else:
        return f'{length1} {unit1} is equal to {length2} {unit2}'
if __name__ == '__main__':
    length1 = 10
    unit1 = 'inches'
    length2 = 25.4
    unit2 = 'cm'
    result = normalize_and_compare(length1, unit1, length2, unit2)
    print(result)