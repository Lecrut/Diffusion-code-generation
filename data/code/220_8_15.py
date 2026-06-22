def average_of_integers(int_list):
    if not hasattr(int_list, '__iter__') or not all(isinstance(x, int) for x in int_list):
        raise ValueError("Input must be an iterable of integers")
    return float(sum(int_list)) / len(int_list)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(average_of_integers(sample_values))