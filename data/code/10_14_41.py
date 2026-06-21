def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return temp1
    elif temp2 > temp1:
        return temp2
    else:
        return temp1
if __name__ == '__main__':
    sample_temp1 = 29.0
    sample_temp2 = 31.5
    higher_temperature = compare_temperatures(sample_temp1, sample_temp2)
    print(higher_temperature)