def filter_duplicates(lst):
    result = []
    seen = set()
    i = 0
    while i < len(lst):
        if lst[i] not in seen:
            result.append(lst[i])
            seen.add(lst[i])
        i += 1
    return result

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(filter_duplicates(sample_list))