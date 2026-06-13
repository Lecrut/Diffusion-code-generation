def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"The largest number in {list1} is: {find_largest(list1)}")
    list2 = [-10, -5, -20, -1]
    print(f"The largest number in {list2} is: {find_largest(list2)}")
    list3 = [42]
    print(f"The largest number in {list3} is: {find_largest(list3)}")
    list4 = [100, 50, 200, 150]
    print(f"The largest number in {list4} is: {find_largest(list4)}")