def convert_and_compare(meter_value1, meter_value2):
    cm_value1 = meter_value1 * 100
    cm_value2 = meter_value2 * 100
    
    if cm_value1 > cm_value2:
        return meter_value1
    else:
        return meter_value2

if __name__ == '__main__':
    value1 = 5.2
    value2 = 3.8
    larger_value = convert_and_compare(value1, value2)
    print(larger_value)