def find_max(lst):
    max_elem = lst[0]
    for elem in lst:
        if elem > max_elem:
            max_elem = elem
    return max_elem

if __name__ == '__main__':
    numbers = [25, 45, 67, 12, 98, 34]
    maximum = find_max(numbers)
    print(maximum)