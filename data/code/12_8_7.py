import statistics

def median_of_sequence(sequence):
    return statistics.median(sequence)

if __name__ == '__main__':
    data_odd = [3, 1, 4, 1, 5]
    data_even = [4, 1, 3, 2]
    
    result_odd = median_of_sequence(data_odd)
    result_even = median_of_sequence(data_even)
    
    print(result_odd)
    print(result_even)