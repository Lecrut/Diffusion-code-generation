def temperature_difference(temp1, temp2):
    difference = abs(temp1 - temp2)
    magnitude_map = {
        (True, True): "Both temperatures are equal",
        (True, False): f"{temp1} is greater than {temp2}",
        (False, True): f"{temp2} is greater than {temp1}"
    }
    key = (temp1 == temp2, temp1 > temp2)
    magnitude = magnitude_map[key]
    return difference, magnitude

if __name__ == '__main__':
    sample_temp1 = 25
    sample_temp2 = 30
    diff, rel_mag = temperature_difference(sample_temp1, sample_temp2)
    print(f"Difference: {diff}")
    print(rel_mag)