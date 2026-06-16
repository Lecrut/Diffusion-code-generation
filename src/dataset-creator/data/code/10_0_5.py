def sort_by_parity(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    odds = [x for x in numbers if x % 2 != 0]
    return evens + odds
if __name__ == '__main__':
    sample_list = [15, -4, 8, 3, 7, 6, 9, 2, 11]
    sort_by_parity(sample_list)