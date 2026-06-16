import sys
def filter_positive(numbers):
    result = []
    for item in numbers:
        if isinstance(item, (int, float)) and item > 0:
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [3.5, -12, "a", None, 7, -4.8, True]
    filtered_list = filter_positive(sample_data)
    print(filtered_list)