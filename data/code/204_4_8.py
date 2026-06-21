import bisect

def get_central_value(sorted_list):
    n = len(sorted_list)
    if n == 0:
        raise ValueError("Cannot find the middle of an empty list")
    return sorted_list[n // 2]

if __name__ == '__main__':
    sample_lists = {
        "list1": [1, 2, 3, 4, 5],
        "list2": [10, 20, 30, 40, 50, 60],
        "list3": [1, 2, 3, 4]
    }
    
    for name, lst in sample_lists.items():
        try:
            print(f"Central value of {lst}: {get_central_value(lst)}")
        except ValueError as e:
            print(e)