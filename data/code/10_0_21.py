def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return (temp1, 'higher')
    elif temp1 < temp2:
        return (temp2, 'lower')
    else:
        return ('equal',)

if __name__ == '__main__':
    temp_a = 36.5
    temp_b = 37.0
    result = compare_temperatures(temp_a, temp_b)
    print(result)