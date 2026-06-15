def find_average(data):
    if not data:
        return 0
    total = 0
    for x in data:
        total += x
    return total / len(data)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    average = find_average(sample_list)
    print(average)
    large_sample_list = list(range(1000000))
    average_large = find_average(large_sample_list)
    print(average_large)
    empty_list = []
    average_empty = find_average(empty_list)
    print(average_empty)