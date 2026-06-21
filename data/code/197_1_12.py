def binary_search_check(checklist, item):
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

if __name__ == '__main__':
    checklist = [3, 5, 7, 9, 11]
    item_to_check = 7
    result = binary_search_check(checklist, item_to_check)
    print(f"Checklist: {checklist}, Item: {item_to_check}, Membership: {result}")
    
    checklist2 = ['apple', 'banana', 'cherry']
    item_to_check2 = 'grape'
    result2 = binary_search_check(checklist2, item_to_check2)
    print(f"Checklist: {checklist2}, Item: {item_to_check2}, Membership: {result2}")
    
    checklist3 = [100, 200, 300, 400, 500]
    item_to_check3 = 350
    result3 = binary_search_check(checklist3, item_to_check3)
    print(f"Checklist: {checklist3}, Item: {item_to_check3}, Membership: {result3}")