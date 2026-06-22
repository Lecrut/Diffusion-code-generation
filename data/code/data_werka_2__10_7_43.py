def check_temperature_difference(temp1, temp2):
    return abs(temp1 - temp2) <= 1

if __name__ == '__main__':
    sample_temp1 = 15.0
    sample_temp2 = 14.8
    result = check_temperature_difference(sample_temp1, sample_temp2)
    print(result)