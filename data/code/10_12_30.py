def temperature_difference(temp1, temp2):
    return abs(temp1 - temp2)

if __name__ == '__main__':
    sample_temp1 = 25.5
    sample_temp2 = 30.7
    print(temperature_difference(sample_temp1, sample_temp2))