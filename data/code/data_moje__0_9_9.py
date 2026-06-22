def convert_lengths(kilometers):
    results = []
    for km in kilometers:
        meters = km * 1000
        feet = km * 3280.84
        results.append((km, meters, feet))
    return results

if __name__ == '__main__':
    sample_km = [1.0, 2.5, 10.0, 0.5]
    converted = convert_lengths(sample_km)
    for original, meters, feet in converted:
        print(f"{original} km = {meters} m = {feet} ft")