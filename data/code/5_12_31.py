def convert_to_cm(meters):
    return meters * 100

def compare_lengths(length1_m, length2_m):
    length1_cm = convert_to_cm(length1_m)
    length2_cm = convert_to_cm(length2_m)
    
    if length1_cm > length2_cm:
        return length1_m
    else:
        return length2_m

if __name__ == '__main__':
    length1 = 5.5
    length2 = 3.8
    larger_length = compare_lengths(length1, length2)
    print(larger_length)