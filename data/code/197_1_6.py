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
    checklist_members = [1, 5, 2, 8, 3]
    item_to_check = 8
    print(f"Item in Checklist: {item_to_check} -> Result: {binary_search(checklist_members, item_to_check)}")
    
    checklist_members = ['a', 'b', 'c']
    item_to_check = 'd'
    print(f"Item in Checklist: {item_to_check} -> Result: {binary_search(checklist_members, item_to_check)}")
    
    checklist_members = [10, 20, 30]
    item_to_check = 20
    print(f"Item in Checklist: {item_to_check} -> Result: {binary_search(checklist_members, item_to_check)}")