import time
def sort_date_strings(date_list):
    start_time = time.time()
    sorted_list = sorted(date_list)
    end_time = time.time()
    return sorted_list, end_time - start_time
if __name__ == '__main__':
    sample_dates = [
        "2023-10-26",
        "2024-01-15",
        "2023-01-01",
        "2024-05-20",
        "2023-10-26",
        "2023-01-01"
    ]
    sorted_dates, elapsed_time = sort_date_strings(sample_dates)
    print(f"Original list: {sample_dates}")
    print(f"Sorted list: {sorted_dates}")
    print(f"Time taken for sorting: {elapsed_time:.6f} seconds")