import bisect

def get_central_value(sorted_list):
    index = len(sorted_list) // 2
    return sorted_list[index]

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(get_central_value(sample_list))