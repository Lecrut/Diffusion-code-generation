def check_equal_sublists(lst):
    for sublist in lst:
        if len(sublist) > 1 and not all(x == sublist[0] for x in sublist):
            return False
    return True
if __name__ == '__main__':
    sample_data = [[1, 2], [3, 3], [4]]
    result = check_equal_sublists(sample_data)
    print(result)