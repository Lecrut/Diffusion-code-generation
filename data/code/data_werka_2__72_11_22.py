def compare_first_and_sixth(lst):
    indices = {'first': 0, 'sixth': 5}
    first_val = lst[indices['first']]
    sixth_val = lst[indices['sixth']]
    return first_val > sixth_val

if __name__ == '__main__':
    sample_data = [100, 10, 20, 30, 40, 50]
    print(compare_first_and_sixth(sample_data))