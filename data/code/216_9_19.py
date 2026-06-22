MIDDLE_INDEX = lambda n: n // 2

def calculate_median(data):
    data.sort()
    n = len(data)
    middle_index = MIDDLE_INDEX(n)
    if n % 2 == 0:
        return (data[middle_index - 1] + data[middle_index]) / 2
    else:
        return data[middle_index]
if __name__ == '__main__':
    sorted_list_even = [2, 4, 6, 8]
    sorted_list_odd = [1, 3, 5, 7, 9]
    print(calculate_median(sorted_list_even))
    print(calculate_median(sorted_list_odd))