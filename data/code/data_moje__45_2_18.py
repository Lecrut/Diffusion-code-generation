def find_min(lst):
    if not lst:
        raise ValueError("List is empty")
    min_val = lst[0]
    for x in lst[1:]:
        if x < min_val:
            min_val = x
    return min_val

if __name__ == '__main__':
    numbers = [3.14, 2.71, 1.41, 4.50, 0.99]
    result = find_min(numbers)
    print(result)