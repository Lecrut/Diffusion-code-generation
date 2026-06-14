def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    list1 = [123456789, 987654321, 555555555]
    list2 = [-100, -5, -1000]
    list3 = [0]
    list4 = [999999999999999999999, 1000000000000000000000, 500000000000000000000]
    list5 = []
    print(f"Largest in {list1}: {find_largest(list1)}")
    print(f"Largest in {list2}: {find_largest(list2)}")
    print(f"Largest in {list3}: {find_largest(list3)}")
    print(f"Largest in {list4}: {find_largest(list4)}")
    try:
        print(f"Largest in {list5}: {find_largest(list5)}")
    except ValueError as e:
        print(e)