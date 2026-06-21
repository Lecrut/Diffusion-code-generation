def binary_search(checklist, item):
    low = 0
    high = len(checklist) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = checklist[mid]
        if guess == item:
            return True
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False

def validate_input(checklist, item):
    if not isinstance(checklist, list) or not all(isinstance(x, (int, str)) for x in checklist):
        raise ValueError("Checklist must be a list of integers or strings")
    if not isinstance(item, (int, str)):
        raise ValueError("Item must be an integer or string")

def check_membership(checklist, item):
    validate_input(checklist, item)
    return binary_search(sorted(checklist), item)

if __name__ == '__main__':
    checklist1 = [1, 5, 2, 8, 3]
    item1 = 8
    print(f"Checklist: {checklist1}, Item: {item1}, Membership: {check_membership(checklist1, item1)}")
    
    checklist2 = ['a', 'b', 'c']
    item2 = 'd'
    print(f"Checklist: {checklist2}, Item: {item2}, Membership: {check_membership(checklist2, item2)}")
    
    checklist3 = [10, 20, 30]
    item3 = 20
    print(f"Checklist: {checklist3}, Item: {item3}, Membership: {check_membership(checklist3, item3)}")