def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return (temp1, 'higher')
    elif temp1 < temp2:
        return (temp2, 'lower')
    else:
        return ('equal',)

if __name__ == '__main__':
    sample_temp1 = 40.0
    sample_temp2 = 38.5
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)