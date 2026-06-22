def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return (temp1, 'higher')
    elif temp1 < temp2:
        return (temp2, 'higher')
    else:
        return ('equal',)

if __name__ == '__main__':
    sample_temp1 = 23.5
    sample_temp2 = 19.8
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)