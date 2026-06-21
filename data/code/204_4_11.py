import bisect

def get_central_value(sorted_list):
    length = len(sorted_list)
    if length % 2 == 0:
        mid1 = length // 2 - 1
        mid2 = length // 2
        return (sorted_list[mid1] + sorted_list[mid2]) / 2
    else:
        mid = length // 2
        return sorted_list[mid]

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(get_central_value(sample_list))