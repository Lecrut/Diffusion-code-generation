def sort_by_parity(arr):
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    return evens + odds
if __name__ == '__main__':
    sample_list = [5, 3, 8, 1, 9, 4, 7, 6, 2]
    sorted_list = sort_by_parity(sample_list)
    print(sorted_list)