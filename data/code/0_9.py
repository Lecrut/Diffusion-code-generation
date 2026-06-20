def convert_measurements(measurements, unit):
    meters = []
    feet = []
    for val in measurements:
        if unit == 'km':
            m = val * 1000
        elif unit == 'cm':
            m = val / 100
        elif unit == 'mm':
            m = val / 1000
        elif unit == 'm':
            m = val
        else:
            m = val
        f = m * 3.28084
        meters.append(m)
        feet.append(f)
    return meters, feet

if __name__ == '__main__':
    samples = [1, 50, 1000]
    unit = 'km'
    m_list, f_list = convert_measurements(samples, unit)
    for original, m, f in zip(samples, m_list, f_list):
        print(f"{original} {unit} = {m} meters = {f} feet")