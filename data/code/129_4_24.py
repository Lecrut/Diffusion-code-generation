def unique_ordered_elements(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 4, 3, 5]
    print(unique_ordered_elements(sample_list))