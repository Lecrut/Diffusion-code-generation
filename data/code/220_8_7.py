def average_of_integers(int_list):
    if not hasattr(int_list, '__iter__'):
        raise ValueError("Input is not iterable")
    
    total = 0
    count = 0
    for num in int_list:
        if isinstance(num, int):
            total += num
            count += 1
        else:
            raise ValueError("List contains non-integer values")
    
    if count == 0:
        raise ValueError("No integer values found in the list")
    
    return float(total) / count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(average_of_integers(sample_list))