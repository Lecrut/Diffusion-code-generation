import statistics

def compute_median(numbers):
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_lists = [
        [1, 3, 2],
        [1, 2, 3, 4],
        [5, 1, 8, 2, 9],
        [10, 20, 30, 40, 50],
        [1, 5, 2, 8, 9]
    ]
    
    for sample_list in sample_lists:
        print(f"Median of {sample_list}: {compute_median(sample_list)}")