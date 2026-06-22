def temperature_difference(temp1, temp2):
    if temp1 > temp2:
        return temp1 - temp2
    else:
        return temp2 - temp1

if __name__ == '__main__':
    sample_temp1 = 50.7
    sample_temp2 = 45.9
    result = temperature_difference(sample_temp1, sample_temp2)
    print(result)