def average_of_sets(list_of_sets):
    if not list_of_sets:
        return None
    total_sum = sum((sum(s) for s in list_of_sets))
    total_count = sum((len(s) for s in list_of_sets))
    if total_count == 0:
        return None
    return total_sum / total_count
if __name__ == '__main__':
    data = [{1, 2, 3}, {4, 5}, {6, 7, 8, 9}]
    avg_result = average_of_sets(data)
    print(avg_result)