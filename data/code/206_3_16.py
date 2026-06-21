def validate_list(lst):
    if not lst:
        raise ValueError("List cannot be empty")

def find_min_item(lst):
    validate_list(lst)
    min_item = lst[0]
    for item in lst[1:]:
        if item < min_item:
            min_item = item
    return min_item

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    minimum_value = find_min_item(sample_list)
    print(minimum_value)