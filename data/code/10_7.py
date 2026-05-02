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
    t1 = 25
    t2 = 35
    diff, rel_mag = temperature_analyzer(t1, t2)
    print(f"Temperatures: {t1}, {t2}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t3 = -10
    t4 = 5
    diff2, rel_mag2 = temperature_analyzer(t3, t4)
    print(f"\nTemperatures: {t3}, {t4}")
    print(f"Difference: {diff2}")
    print(f"Relative Magnitude: {rel_mag2}")
    t5 = 0
    t6 = 0
    diff3, rel_mag3 = temperature_analyzer(t5, t6)
    print(f"\nTemperatures: {t5}, {t6}")
    print(f"Difference: {diff3}")
    print(f"Relative Magnitude: {rel_mag3}")
    t7 = 100
    t8 = 101
    diff4, rel_mag4 = temperature_analyzer(t7, t8)
    print(f"\nTemperatures: {t7}, {t8}")
    print(f"Difference: {diff4}")
    print(f"Relative Magnitude: {rel_mag4}")