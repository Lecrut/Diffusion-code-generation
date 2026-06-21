def quicksort(items):
    if not all(isinstance(x, int) for x in items):
        raise ValueError("All elements must be integers")
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    middle = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    data = [5, 2, 8, 1, 9]
    sorted_data = quicksort(data)
    print(sorted_data)