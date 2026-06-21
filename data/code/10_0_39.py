def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return (temp1, 'higher')
    elif temp1 < temp2:
        return (temp2, 'lower')
    else:
        return ('equal',)

if __name__ == '__main__':
    sample_temp1 = 30.5
    sample_temp2 = 28.9
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)

    sample_temp3 = 22.0
    sample_temp4 = 22.0
    result = compare_temperatures(sample_temp3, sample_temp4)
    print(result)

    sample_temp5 = 15.7
    sample_temp6 = 18.3
    result = compare_temperatures(sample_temp5, sample_temp6)
    print(result)