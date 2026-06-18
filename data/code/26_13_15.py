def check_first_greater_than_second(lst):
    return lambda: lst[0] > lst[1] if len(lst) >= 2 else None

if __name__ == '__main__':
    sample_list = [5, 3]
    result = check_first_greater_than_second(sample_list)()
    print(result)