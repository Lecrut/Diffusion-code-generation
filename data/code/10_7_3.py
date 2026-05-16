def temperature_analyzer(temp1, temp2):
    difference = abs(temp1 - temp2)
    if temp1 == 0 and temp2 == 0:
        relative_magnitude = 0.0
    elif temp1 == 0 or temp2 == 0:
        relative_magnitude = float('inf')
    else:
        average = (temp1 + temp2) / 2
        relative_magnitude = difference / average
    return difference, relative_magnitude
if __name__ == '__main__':
    t1 = 25
    t2 = 35
    diff, rel_mag = temperature_analyzer(t1, t2)
    print(f"Temperatures: {t1}, {t2}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t3 = 10
    t4 = 10
    diff, rel_mag = temperature_analyzer(t3, t4)
    print(f"\nTemperatures: {t3}, {t4}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t5 = 50
    t6 = 10
    diff, rel_mag = temperature_analyzer(t5, t6)
    print(f"\nTemperatures: {t5}, {t6}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t7 = 0
    t8 = 0
    diff, rel_mag = temperature_analyzer(t7, t8)
    print(f"\nTemperatures: {t7}, {t8}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t9 = 20
    t10 = 0
    diff, rel_mag = temperature_analyzer(t9, t10)
    print(f"\nTemperatures: {t9}, {t10}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")