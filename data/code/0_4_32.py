def meters_to_yards(meters):
    return meters * 1.09361

if __name__ == '__main__':
    sample_lengths = [1, 10, 100]
    
    for length in sample_lengths:
        yards = meters_to_yards(length)
        print(yards)