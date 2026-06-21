def filter_duplicates(lst):
    seen = set()
    result = []
    i = 0
    while i < len(lst):
        if lst[i] not in seen:
            seen.add(lst[i])
            result.append(lst[i])
        i += 1
    return result

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(filter_duplicates(sample_list))