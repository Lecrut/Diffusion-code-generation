def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return temp1
    return temp2

if __name__ == '__main__':
    sample_temp1 = 18.3
    sample_temp2 = 22.7
    higher_temperature = compare_temperatures(sample_temp1, sample_temp2)
    print(higher_temperature)