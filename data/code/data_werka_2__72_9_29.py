COMPARISON_RESULT = "equal"
COMPARISON_GREAT = "greater than"
COMPARISON_SMALL = "less than"
RESULT_FORMAT = "{0} {1} {2}"

def compare_elements(lst, idx1, idx2):
    length = len(lst)
    if not (0 <= idx1 < length):
        return None
    if not (0 <= idx2 < length):
        return None
    value_first = lst[idx1]
    value_second = lst[idx2]
    if value_first > value_second:
        return COMPARISON_GREAT
    if value_first < value_second:
        return COMPARISON_SMALL
    return COMPARISON_RESULT

if __name__ == '__main__':
    data = [5, 15, 10, 25, 20]
    output = compare_elements(data, 0, 2)
    print(output)
    output2 = compare_elements(data, 3, 4)
    print(output2)
    output3 = compare_elements(data, 0, 1)
    print(output3)