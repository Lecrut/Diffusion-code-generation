def convert_to_centimeters(meters):
    return meters * 100

def compare_lengths(length1_m, length2_m):
    length1_cm = convert_to_centimeters(length1_m)
    length2_cm = convert_to_centimeters(length2_m)
    
    if length1_cm > length2_cm:
        return length1_m
    else:
        return length2_m

if __name__ == '__main__':
    sample_length1 = 4.9
    sample_length2 = 6.3
    larger_value = compare_lengths(sample_length1, sample_length2)
    print(larger_value)