def temperature_difference(temp1, temp2):
    difference = abs(temp1 - temp2)
    magnitude_map = {(True, True): 'both temperatures are equal', (True, False): f'{temp1} is greater than {temp2}', (False, True): f'{temp2} is greater than {temp1}'}
    if temp1 > temp2:
        magnitude = magnitude_map[temp1 == temp2, False]
    elif temp1 < temp2:
        magnitude = magnitude_map[False, temp1 == temp2]
    else:
        magnitude = magnitude_map[True, True]
    return (difference, magnitude)
if __name__ == '__main__':
    sample_temp1 = 25
    sample_temp2 = 30
    diff, rel_mag = temperature_difference(sample_temp1, sample_temp2)
    print(f'Difference: {diff}')
    print(rel_mag)