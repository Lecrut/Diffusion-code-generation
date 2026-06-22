def compare_temperatures(temp1, temp2):
    return temp1 if temp1 > temp2 else temp2

if __name__ == '__main__':
    sample_temp1 = 35.0
    sample_temp2 = 31.4
    higher_temperature = compare_temperatures(sample_temp1, sample_temp2)
    print(higher_temperature)