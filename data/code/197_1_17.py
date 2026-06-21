def binary_search(checklist, item):
    low = 0
    high = len(checklist) - 1

    while low <= high:
        mid = (low + high) // 2
        if checklist[mid] == item:
            return True
        elif checklist[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return False

if __name__ == '__main__':
    checklist1 = [1, 5, 2, 8, 3]
    item1 = 8
    print(f"Checklist: {checklist1}, Item: {item1}, Found: {binary_search(sorted(checklist1), item1)}")
    
    checklist2 = ['a', 'b', 'c']
    item2 = 'd'
    print(f"Checklist: {checklist2}, Item: {item2}, Found: {binary_search(sorted(checklist2), item2)}")
    
    checklist3 = [10, 20, 30]
    item3 = 20
    print(f"Checklist: {checklist3}, Item: {item3}, Found: {binary_search(sorted(checklist3), item3)}")