MIN_VALUE = float('inf')
MAX_VALUE = float('-inf')

def find_min_max(data):
    minimum = MIN_VALUE
    maximum = MAX_VALUE
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum

if __name__ == '__main__':
    sample_list1 = [5.5, 2.3, 9.8, 1.7, 7.4]
    sample_list2 = [-10.2, 5.1, 0.6, -3.9, 8.7]
    sample_list3 = [42.0]

    min_val1, max_val1 = find_min_max(sample_list1)
    min_val2, max_val2 = find_min_max(sample_list2)
    min_val3, max_val3 = find_min_max(sample_list3)

    print(f"List 1: Min={min_val1}, Max={max_val1}")
    print(f"List 2: Min={min_val2}, Max={max_val2}")
    print(f"List 3: Min={min_val3}, Max={max_val3}")