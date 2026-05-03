def temperature_analyzer(temp1, temp2):
    difference = abs(temp1 - temp2)
    if temp1 == 0 and temp2 == 0:
        relative_magnitude = 0.0
    elif temp1 == 0 or temp2 == 0:
        relative_magnitude = float('inf')
    else:
        magnitude = max(abs(temp1), abs(temp2))
        relative_magnitude = difference / magnitude
    return difference, relative_magnitude
if __name__ == '__main__':
    t1 = 25.5
    t2 = 15.0
    diff, rel_mag = temperature_analyzer(t1, t2)
    print(f"Temperature 1: {t1}, Temperature 2: {t2}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t3 = -10.0
    t4 = -5.0
    diff, rel_mag = temperature_analyzer(t3, t4)
    print(f"\nTemperature 3: {t3}, Temperature 4: {t4}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t5 = 0.0
    t6 = 0.0
    diff, rel_mag = temperature_analyzer(t5, t6)
    print(f"\nTemperature 5: {t5}, Temperature 6: {t6}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t7 = 50.0
    t8 = 10.0
    diff, rel_mag = temperature_analyzer(t7, t8)
    print(f"\nTemperature 7: {t7}, Temperature 8: {t8}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")