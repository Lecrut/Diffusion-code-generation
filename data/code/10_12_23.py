def temperature_difference(temp1, temp2):
    return abs(temp1 - temp2)

if __name__ == '__main__':
    sample_temp1 = 30.5
    sample_temp2 = 25.8
    print(temperature_difference(sample_temp1, sample_temp2))