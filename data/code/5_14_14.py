def normalize_to_centimeters(length, unit):
    if unit == 'inches':
        return length * 2.54
    elif unit == 'centimeters':
        return length
    else:
        raise ValueError('Unsupported unit')

def compare_lengths(length_a, unit_a, length_b, unit_b):
    cm_a = normalize_to_centimeters(length_a, unit_a)
    cm_b = normalize_to_centimeters(length_b, unit_b)
    if cm_a > cm_b:
        return f'{length_a} {unit_a} is greater than {length_b} {unit_b}'
    elif cm_a < cm_b:
        return f'{length_a} {unit_a} is less than {length_b} {unit_b}'
    else:
        return f'{length_a} {unit_a} is equal to {length_b} {unit_b}'

if __name__ == '__main__':
    sample_length_1 = 10
    sample_unit_1 = 'inches'
    sample_length_2 = 25.4
    sample_unit_2 = 'centimeters'
    result = compare_lengths(sample_length_1, sample_unit_1, sample_length_2, sample_unit_2)
    print(result)