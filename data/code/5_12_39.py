def convert_and_compare(meters1, meters2):
    cm1 = meters1 * 100
    cm2 = meters2 * 100
    
    if cm1 > cm2:
        return meters1
    else:
        return meters2

if __name__ == '__main__':
    length_a = 7.2
    length_b = 4.9
    larger_length = convert_and_compare(length_a, length_b)
    print(larger_length)