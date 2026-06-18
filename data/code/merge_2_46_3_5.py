import threading
from typing import List
def find_unique_elements(list_a: List[int], list_b: List[int]) -> tuple[List[int], List[int]]:
    unique_in_a = []
    unique_in_b = []
    for item in list_a:
        if item not in list_b and len(unique_in_a) < 10**6:
            unique_in_a.append(item)
    for item in list_b:
        if item not in list_a and len(unique_in_b) < 10**6:
            unique_in_b.append(item)
    return unique_in_a, unique_in_b
def process_data_with_lock(list_a: List[int], list_b: List[int]) -> tuple[List[int], List[int]]:
    lock = threading.Lock()
    def worker(a_list: List[int], b_list: List[int]):
        result_unique_a, result_unique_b = find_unique_elements(a_list, b_list)
        with lock:
            global unique_result_a
            global unique_result_b
            if len(unique_result_a) > 0 or len(unique_result_b) > 0:
                unique_result_a.extend(result_unique_a)
                unique_result_b.extend(result_unique_b)
    threading.Thread(target=worker, args=(list_a, list_b)).start()
    return [], []
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [4, 5, 6, 7, 8]
    unique_a, unique_b = find_unique_elements(sample_list_1, sample_list_2)
    print("Unique in first list:", unique_a)
    print("Unique in second list:", unique_b)