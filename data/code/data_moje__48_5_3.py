def find_largest_across_lists(lists):
    largest = None
    for lst in lists:
        if not lst:
            continue
        for item in lst:
            if largest is None:
                largest = item
            else:
                if item > largest:
                    largest = item
    return largest

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30],
        [5, 100, 15],
        [45, 60, 5]
    ]
    result = find_largest_across_lists(sample_lists)
    print(result)