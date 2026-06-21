MIN_VALUE = float('inf')

def find_min_item(lst):
    if not lst:
        raise ValueError('List is empty')
    min_item = MIN_VALUE
    for item in lst:
        if item < min_item:
            min_item = item
    return min_item

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_min_item(sample_list))