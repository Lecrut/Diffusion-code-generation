def quicksort(items):
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    middle = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    sample_data = [3, 6, 8, 10, 1, 2, 1]
    sorted_data = quicksort(sample_data)
    print(sorted_data)