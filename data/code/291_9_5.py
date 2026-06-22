def compare_lengths(rod_length, meter_length):
    rod_to_meter = 5.0292
    converted_rod_length = rod_length * rod_to_meter
    if converted_rod_length == meter_length:
        return 'Equal lengths'
    elif converted_rod_length < meter_length:
        return 'Rod length is shorter'
    else:
        return 'Rod length is longer'
if __name__ == '__main__':
    print(compare_lengths(10, 50.292))
    print(compare_lengths(8, 40.2336))
    print(compare_lengths(12, 60.3504))