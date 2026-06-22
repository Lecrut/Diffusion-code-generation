def get_last_element(lst):
    return lst[-1:]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    last = get_last_element(sample_list)
    print(last[0] if last else None)