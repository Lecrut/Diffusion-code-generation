METERS_PER_YARD = 0.9144
KILOMETERS_PER_METER = 1 / 1000

def yards_to_kilometers(yards):
    meters = yards * METERS_PER_YARD
    kilometers = meters * KILOMETERS_PER_METER
    return kilometers

if __name__ == '__main__':
    sample_yard_values = [1, 2.5, 10, 100]
    for yard in sample_yard_values:
        print(f"{yard} yards is {yards_to_kilometers(yard):.4f} kilometers")