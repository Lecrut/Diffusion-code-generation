def convert_and_compare(m1, m2):
    def meters_to_cm(meters):
        return meters * 100
    
    cm1 = meters_to_cm(m1)
    cm2 = meters_to_cm(m2)
    
    if cm1 > cm2:
        return m1
    else:
        return m2

if __name__ == '__main__':
    value1 = 4.5
    value2 = 6.3
    larger_value = convert_and_compare(value1, value2)
    print(larger_value)