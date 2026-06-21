def get_last_element(lst):
    return next(reversed(lst))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(get_last_element(sample_data))