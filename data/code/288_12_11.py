def convert_to_celsius(temp, scale):
    if scale == 'C':
        return temp
    elif scale == 'F':
        return (temp - 32) * 5 / 9
    elif scale == 'K':
        return temp - 273.15

def average_temperature(temp1, scale1, temp2, scale2, temp3, scale3):
    temp1_c = convert_to_celsius(temp1, scale1)
    temp2_c = convert_to_celsius(temp2, scale2)
    temp3_c = convert_to_celsius(temp3, scale3)
    return (temp1_c + temp2_c + temp3_c) / 3

if __name__ == '__main__':
    print(average_temperature(0, 'C', 32, 'F', 273.15, 'K'))