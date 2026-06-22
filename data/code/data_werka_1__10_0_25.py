def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return ('higher', temp1)
    elif temp1 < temp2:
        return ('lower', temp2)
    else:
        return ('equal', temp1)

if __name__ == '__main__':
    sample_temp1 = 98.6
    sample_temp2 = 100.0
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)