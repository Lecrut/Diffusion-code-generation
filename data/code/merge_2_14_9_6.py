import sys
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    unique_elements = remove_duplicates(sample_list)
    print(unique_elements)