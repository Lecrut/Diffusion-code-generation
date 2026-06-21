def filter_odd(numbers):
    return [x for x in numbers if x % 2 != 0]

if __name__ == '__main__':
    sample_values = [12, 17, 19, 21, 23, 24, 25]
    filtered_odds = filter_odd(sample_values)
    print(filtered_odds)