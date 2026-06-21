import statistics

def compute_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return statistics.median(data)

if __name__ == '__main__':
    sample_list_odd = [1, 5, 3, 7, 9]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [42]
    sample_list_empty = []
    
    try:
        print(f"Median of {sample_list_odd}: {compute_median(sample_list_odd)}")
        print(f"Median of {sample_list_even}: {compute_median(sample_list_even)}")
        print(f"Median of {sample_list_single}: {compute_median(sample_list_single)}")
        print(f"Median of {sample_list_empty}: {compute_median(sample_list_empty)}")
    except ValueError as e:
        print(e)