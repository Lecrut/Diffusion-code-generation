def meters_to_yards(meters):
    return meters * 1.09361

if __name__ == '__main__':
    lengths = [1, 10, 100]
    for length in lengths:
        yards = meters_to_yards(length)
        print(yards)