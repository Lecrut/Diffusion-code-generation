def first_greater_than_second(lst):
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3]
    result = first_greater_than_second(sample_list)
    print(result)