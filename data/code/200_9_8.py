def unique_values(lst):
    return dict.fromkeys(lst).keys()

if __name__ == '__main__':
    sample_list = [4, 5, 6, 4, 3, 2, 1, 6]
    print(unique_values(sample_list))