import math

def convert_meters_to_yards(meters_list):
    return [m * 1.09361 for m in meters_list]

if __name__ == '__main__':
    sample_lengths = [1.0, 2.5, 100.0, 0.5]
    result = convert_meters_to_yards(sample_lengths)
    print(result)