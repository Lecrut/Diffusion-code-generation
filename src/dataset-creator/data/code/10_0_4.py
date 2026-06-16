def sort_by_parity(arr):
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    evens.sort(reverse=True)
    odds.sort()
    return evens + odds
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3, 4]
    sorted_list = sort_by_parity(sample_list.copy())
    print(sorted_list)