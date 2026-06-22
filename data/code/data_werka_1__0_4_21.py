def meters_to_yards(lengths: list) -> list:
    return [length * 1.09361 for length in lengths]

if __name__ == '__main__':
    sample_lengths = [1, 5, 10, 100]
    yards = meters_to_yards(sample_lengths)
    for original, converted in zip(sample_lengths, yards):
        print(f"{original} meters is {converted} yards")