import time
def sort_and_analyze(items):
    start_time = time.time()
    sorted_items = sorted(items)
    end_time = time.time()
    print("Sorted items:", sorted_items)
    print("Time taken:", end_time - start_time)
if __name__ == '__main__':
    sample_data = [3.14, 1.0, 5, 2.718, 0.5]
    sort_and_analyze(sample_data)