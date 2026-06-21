import bisect

def get_central_value(sorted_list):
    n = len(sorted_list)
    if n == 0:
        raise ValueError("Cannot find the middle of an empty list")
    middle_index = n // 2
    return sorted_list[middle_index]

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9, 11]
    print(f"Central value of {sample_list}: {get_central_value(sample_list)}")