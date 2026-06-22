def validate_list(lst):
    return len(lst) >= 2

def get_second_item(lst):
    if not validate_list(lst):
        return None
    return lst[1]

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30, 40, 50],
        [5],
        ['a', 'b', 'c'],
        []
    ]
    for i, lst in enumerate(sample_lists):
        print(f"The second item in list {i+1} is: {get_second_item(lst)}")