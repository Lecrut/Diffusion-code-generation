import sys
import io

def convert_lengths(lengths, unit):
    km_to_m = 1000.0
    m_to_ft = 3.28084

    results = []
    for length in lengths:
        if unit.lower() == 'km':
            meters = length * km_to_m
        elif unit.lower() == 'm':
            meters = length
        elif unit.lower() == 'ft':
            meters = length / m_to_ft
        else:
            meters = None

        if meters is not None:
            feet = meters * m_to_ft
        else:
            feet = None

        results.append((meters, feet))

    return results

if __name__ == '__main__':
    sample_lengths = [1.5, 3.0, 7.25, 10.0]
    sample_unit = 'km'

    converted = convert_lengths(sample_lengths, sample_unit)

    for length, (meters, feet) in zip(sample_lengths, converted):
        print(f"{length} {sample_unit} = {meters:.4f} m = {feet:.4f} ft")