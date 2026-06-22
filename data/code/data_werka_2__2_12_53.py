def cubic_meters_to_cubic_feet(meters):
    if meters < 0:
        raise ValueError("Volume cannot be negative")
    return meters * 35.3146667

if __name__ == '__main__':
    sample_values = [1, 2.5, 10]
    for value in sample_values:
        print(f"{value} cubic meters is {cubic_meters_to_cubic_feet(value)} cubic feet")