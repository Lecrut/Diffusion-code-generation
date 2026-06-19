def compare_lengths(length1_meters, length2_meters):
    length1_cm = length1_meters * 100
    length2_cm = length2_meters * 100
    
    if length1_cm > length2_cm:
        return length1_meters
    else:
        return length2_meters

if __name__ == '__main__':
    sample_length1 = 5.2
    sample_length2 = 3.8
    larger_length = compare_lengths(sample_length1, sample_length2)
    print(larger_length)