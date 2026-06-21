import statistics

def calculate_median(numbers):
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_lists = [
        [1, 3, 2],
        [1, 2, 3, 4],
        [5, 1, 8, 2, 9],
        [10, 20, 30, 40, 50]
    ]
    
    for lst in sample_lists:
        print(f"Median of {lst}: {calculate_median(lst)}")