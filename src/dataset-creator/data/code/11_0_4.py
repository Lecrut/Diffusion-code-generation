def check_equal_sublists(data):
    for sublist in data:
        if len(sublist) > 1 and not all(x == sublist[0] for x in sublist):
            return False
    return True
if __name__ == '__main__':
    sample_data = [[1, 2], [3, 3], [], [4, 5]]
    result = check_equal_sublists(sample_data)
    print(result)