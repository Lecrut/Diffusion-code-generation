import sys
def calculate_center(iterable):
    total = sum(1 for _ in iterable)
    if total == 0:
        return None
    half = (total + 1) // 2
    iterator = iter(iterable)
    try:
        for _ in range(half - 1):
            next(iterator)
        center_element = next(iterator)
        if total % 2 == 0 and half < total:
            right_half_start = next(iterator)
            return (center_element + right_half_start) / 2
        else:
            return center_element
    except StopIteration:
        return None
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = calculate_center(sample_list)
    print(result)