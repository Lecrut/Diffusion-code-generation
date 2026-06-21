def binary_search(item, checklist):
    low = 0
    high = len(checklist) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = checklist[mid]
        if guess == item:
            return True
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False
if __name__ == '__main__':
    checklist = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(binary_search('banana', checklist))
    print(binary_search('grape', checklist))