def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return temp1
    else:
        return temp2

if __name__ == '__main__':
    sample_temp1 = 30.2
    sample_temp2 = 27.6
    higher_temperature = compare_temperatures(sample_temp1, sample_temp2)
    print(higher_temperature)