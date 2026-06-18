def sort_by_parity(arr):
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    return evens + odds
if __name__ == '__main__':
    sample_list = [1, 4, 3, 8, 5, 9, 6, 7]
    sorted_list = sort_by_parity(sample_list)