def convert_to_centimeters(length, unit):
    if unit == 'inches':
        return length * 2.54
    elif unit == 'centimeters':
        return length
    else:
        raise ValueError('Unsupported unit')

def compare_lengths(length1, unit1, length2, unit2):
    length1_cm = convert_to_centimeters(length1, unit1)
    length2_cm = convert_to_centimeters(length2, unit2)
    
    if length1_cm > length2_cm:
        return 'Length 1 is greater than Length 2'
    elif length1_cm < length2_cm:
        return 'Length 2 is greater than Length 1'
    else:
        return 'Both lengths are equal'

if __name__ == '__main__':
    inches_value = 10
    centimeters_value = 25.4
    result = compare_lengths(inches_value, 'inches', centimeters_value, 'centimeters')
    print(result)