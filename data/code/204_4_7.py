import bisect

def get_central_value(sorted_list):
    length = len(sorted_list)
    if length % 2 == 0:
        return (sorted_list[length // 2 - 1] + sorted_list[length // 2]) / 2
    else:
        return sorted_list[length // 2]

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(get_central_value(sample_list))