def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(remove_duplicates(sample_list))