def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = max(numbers)
    return largest

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -20, -1]
    list3 = [7]
    list4 = []
    try:
        print(f"Largest in {list1}: {find_largest(list1)}")
        print(f"Largest in {list2}: {find_largest(list2)}")
        print(f"Largest in {list3}: {find_largest(list3)}")
        print(f"Largest in {list4}: {find_largest(list4)}")
    except ValueError as e:
        print(e)