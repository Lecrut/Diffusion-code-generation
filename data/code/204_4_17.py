import bisect

MIDDLE_INDEX = lambda n: n // 2

def get_central_value(sorted_list):
    n = len(sorted_list)
    if n == 0:
        raise ValueError("Cannot find the middle of an empty list")
    return sorted_list[MIDDLE_INDEX(n)]

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(f"Central value of {sample_list}: {get_central_value(sample_list)}")

    sample_list = [5, 7, 9, 11, 13, 15]
    central_value = get_central_value(sample_list)
    print(f"Central value of {sample_list}: {central_value}")

    sample_list = [1, 2, 3, 4]
    try:
        print(f"Central value of {sample_list}: {get_central_value(sample_list)}")
    except ValueError as e:
        print(e)