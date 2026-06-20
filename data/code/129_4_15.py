def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 7, 3, 5]
    unique_list = remove_duplicates(sample_list)
    print(unique_list)