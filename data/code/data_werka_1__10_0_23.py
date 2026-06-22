def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return (temp1, 'higher')
    elif temp1 < temp2:
        return (temp2, 'lower')
    else:
        return ('equal',)
if __name__ == '__main__':
    result = compare_temperatures(30.5, 28.9)
    print(result)
    result = compare_temperatures(22.0, 22.0)
    print(result)
    result = compare_temperatures(15.7, 18.3)
    print(result)