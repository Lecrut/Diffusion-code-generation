import time
def compare_and_report(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 >= sum2:
        return sum1, list1
    else:
        return sum2, list2
if __name__ == '__main__':
    list_a = [1, 5, 10, 2]
    list_b = [3, 7, 4, 1]
    start_time = time.perf_counter()
    result_sum, winning_list = compare_and_report(list_a, list_b)
    end_time = time.perf_counter()
    print(f"Sum of List A: {result_sum}")
    print(f"List A: {winning_list}")
    print(f"Time taken: {(end_time - start_time):.6f} seconds")