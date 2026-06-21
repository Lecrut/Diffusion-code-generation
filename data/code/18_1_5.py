def get_median(numbers):
    length = len(numbers)
    if length == 0:
        return None
    mid_index = length // 2
    if length % 2 == 0:
        val1 = numbers[mid_index - 1]
        val2 = numbers[mid_index]
        return (val1 + val2) / 2
    return numbers[mid_index]

if __name__ == '__main__':
    sorted_list_even = [1, 3, 5, 7]
    sorted_list_odd = [2, 4, 6, 8, 10]
    median_even = get_median(sorted_list_even)
    median_odd = get_median(sorted_list_odd)
    print(median_even)
    print(median_odd)