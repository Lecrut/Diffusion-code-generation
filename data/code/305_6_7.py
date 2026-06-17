import time
def sort_date_strings(date_list):
    return sorted(date_list)
if __name__ == '__main__':
    sample_dates = [
        "2023-10-26",
        "2024-01-15",
        "2023-12-31",
        "2023-10-01",
        "2024-01-01",
        "2023-11-11"
    ]
    start_time = time.perf_counter()
    sorted_dates = sort_date_strings(sample_dates)
    end_time = time.perf_counter()
    print(sorted_dates)
    print(f"Sorting time: {end_time - start_time:.6f} seconds")