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
    checklist = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    item_to_check = 'banana'
    print(binary_search(checklist, item_to_check))