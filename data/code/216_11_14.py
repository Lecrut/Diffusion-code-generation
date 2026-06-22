MIDDLE_INDEX = lambda n: n // 2

def find_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[MIDDLE_INDEX(n)]
    else:
        lower_middle_index = MIDDLE_INDEX(n) - 1
        upper_middle_index = MIDDLE_INDEX(n)
        return (sorted_data[lower_middle_index] + sorted_data[upper_middle_index]) / 2

if __name__ == '__main__':
    sample_list = [4, 7, 2, 5, 8]
    print(find_median(sample_list))