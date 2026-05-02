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
    t_a = 25.5
    t_b = 15.0
    diff, rel_mag = temperature_analyzer(t_a, t_b)
    print(f"Temperature 1: {t_a}, Temperature 2: {t_b}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t_c = -10.0
    t_d = -10.0
    diff, rel_mag = temperature_analyzer(t_c, t_d)
    print(f"\nTemperature 1: {t_c}, Temperature 2: {t_d}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t_e = 50.0
    t_f = 10.0
    diff, rel_mag = temperature_analyzer(t_e, t_f)
    print(f"\nTemperature 1: {t_e}, Temperature 2: {t_f}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")
    t_g = 0.0
    t_h = 5.0
    diff, rel_mag = temperature_analyzer(t_g, t_h)
    print(f"\nTemperature 1: {t_g}, Temperature 2: {t_h}")
    print(f"Difference: {diff}")
    print(f"Relative Magnitude: {rel_mag}")