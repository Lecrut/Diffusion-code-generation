def convert_lengths(lengths, from_unit):
    meters = []
    feet = []
    for length in lengths:
        if from_unit.lower() == "kilometers":
            length_in_meters = length * 1000
        elif from_unit.lower() == "miles":
            length_in_meters = length * 1609.344
        elif from_unit.lower() == "feet":
            length_in_meters = length * 0.3048
        else:
            length_in_meters = length
        length_in_feet = length_in_meters / 0.3048
        meters.append(length_in_meters)
        feet.append(length_in_feet)
    return meters, feet

if __name__ == '__main__':
    sample_lengths = [1.0, 5.5, 10.0]
    source_unit = "kilometers"
    meters_results, feet_results = convert_lengths(sample_lengths, source_unit)
    for original, in_meters, in_feet in zip(sample_lengths, meters_results, feet_results):
        print(f"{original} {source_unit} = {in_meters} meters = {in_feet} feet")