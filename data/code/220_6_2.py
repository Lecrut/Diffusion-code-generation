def sum_and_count_sets(list_of_sets):
    total_sum = 0
    total_count = 0
    for s in list_of_sets:
        total_sum += sum(s)
        total_count += len(s)
    yield total_sum
    yield total_count
if __name__ == '__main__':
    data = [
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    ]
    results_generator = sum_and_count_sets(data)
    total_sum_result = 0
    total_count_result = 0
    for result in results_generator:
        if isinstance(result, int):
            if total_sum_result == 0:
                total_sum_result = result
            else:
                total_count_result = result
        else:
            total_sum_result = result
    if total_count_result > 0:
        average = total_sum_result / total_count_result
        print(f"Total Sum: {total_sum_result}")
        print(f"Total Count: {total_count_result}")
        print(f"Average: {average}")
    else:
        print("Total count is zero, cannot calculate average.")