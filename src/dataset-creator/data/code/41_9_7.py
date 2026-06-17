import time
from collections import Counter
def count_sparse_items(matrix_list):
    return len(Counter(item for row in matrix_list for item in row))
if __name__ == '__main__':
    sample_data = [
        [10], 
        [20], 
        [30, 40], 
        [], 
        [50]
    ] * 9                                            
    start_time = time.perf_counter()
    result_count = count_sparse_items(sample_data)
    end_time = time.perf_counter()
    print(f"Total items counted: {result_count}")