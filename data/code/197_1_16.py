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
    checklist_members = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    item1 = 'banana'
    print(f"Checklist: {checklist_members}, Item: {item1}, Exists: {binary_search(checklist_members, item1)}")
    
    item2 = 'fig'
    print(f"Checklist: {checklist_members}, Item: {item2}, Exists: {binary_search(checklist_members, item2)}")