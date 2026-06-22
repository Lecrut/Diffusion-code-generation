def meters_to_yards(lengths_meters):
    return [length * 1.09361 for length in lengths_meters]

if __name__ == '__main__':
    sample_lengths = [1, 10, 100, 0.5]
    yards = meters_to_yards(sample_lengths)
    for m, y in zip(sample_lengths, yards):
        print(f"{m} meters is {y} yards")