def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return 'First temperature is greater.'
    elif temp1 < temp2:
        return 'Second temperature is greater.'
    else:
        return 'Both temperatures are equal.'
assert compare_temperatures(30, 25) == 'First temperature is greater.'
assert compare_temperatures(20, 25) == 'Second temperature is greater.'
assert compare_temperatures(15, 15) == 'Both temperatures are equal.'
if __name__ == '__main__':
    temp_a = 28
    temp_b = 32
    result = compare_temperatures(temp_a, temp_b)
    print(result)