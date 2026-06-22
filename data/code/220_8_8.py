def average_of_integers(int_list):
    if not hasattr(int_list, '__iter__'):
        raise ValueError("Input must be an iterable")
    total = sum(int_list)
    count = len(int_list)
    return float(total) / count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(average_of_integers(sample_list))