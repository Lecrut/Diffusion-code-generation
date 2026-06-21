class ListComparator:
    COMPARE_FIRST_GREATER = lambda lst: lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [7, 4]
    result = ListComparator.COMPARE_FIRST_GREATER(sample_list)
    print(result)