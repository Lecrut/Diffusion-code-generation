def set_sum_count_generator(list_of_sets):
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
    results = set_sum_count_generator(data)
    total_sum = None
    total_count = None
    for result in results:
        if total_sum is None:
            total_sum = result
        else:
            total_count = result
    if total_count > 0:
        average = total_sum / total_count
        print(f"Total Sum: {total_sum}")
        print(f"Total Count: {total_count}")
        print(f"Average: {average}")
    else:
        print("Total count is zero, cannot calculate average.")