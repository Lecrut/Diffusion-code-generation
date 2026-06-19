def meters_to_yards(meters):
    return meters * 1.09361

if __name__ == '__main__':
    lengths_in_meters = [1, 10, 100, 1000]
    
    for length in lengths_in_meters:
        yards = meters_to_yards(length)
        print(yards)