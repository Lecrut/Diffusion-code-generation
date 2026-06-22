def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return (temp1, 'higher')
    elif temp1 < temp2:
        return (temp2, 'lower')
    else:
        return (temp1, 'equal')

if __name__ == '__main__':
    sample_temp1 = 36.8
    sample_temp2 = 37.5
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)