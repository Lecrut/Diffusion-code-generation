KM_TO_METER = 1000.0
METER_TO_FOOT = 3.28084

def convert_measurements(lengths_km):
    results = []
    for km in lengths_km:
        meters = km * KM_TO_METER
        feet = meters * METER_TO_FOOT
        results.append((meters, feet))
    return results

if __name__ == '__main__':
    sample_lengths = [1.0, 5.5, 10.0, 0.25]
    converted = convert_measurements(sample_lengths)
    for km, (m, f) in zip(sample_lengths, converted):
        print(f"{km} km = {m} m = {f} ft")