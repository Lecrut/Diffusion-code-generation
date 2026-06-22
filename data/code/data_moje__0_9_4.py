def convert_lengths(lengths_km):
    results = []
    for km in lengths_km:
        meters = km * 1000.0
        feet = meters / 0.3048
        results.append((km, meters, feet))
    return results

if __name__ == '__main__':
    sample_km = [1.0, 2.5, 0.5, 10.0]
    conversions = convert_lengths(sample_km)
    for km, meters, feet in conversions:
        print(f"{km} km = {meters} m = {feet} ft")