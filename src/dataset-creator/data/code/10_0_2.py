def sort_by_parity(nums):
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    return evens + odds
if __name__ == '__main__':
    sample_list = [5, 3, 8, 12, 7, 4, 9, 6]
    sorted_list = sort_by_parity(sample_list)
    print(sorted_list)