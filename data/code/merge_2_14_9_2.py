from collections import OrderedDict
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_list = [5, 23, 45, 78, 90, 12, 45, 67, 89, 12]
    unique_elements = remove_duplicates(sample_list)
    print(unique_elements)