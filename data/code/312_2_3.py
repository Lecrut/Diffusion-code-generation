def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 8, 15]
    sample_list2 = [-5, -1, -10, -3]
    sample_list3 = [42]
    sample_list4 = []
    print(f"Largest in {sample_list1}: {find_largest(sample_list1)}")
    print(f"Largest in {sample_list2}: {find_largest(sample_list2)}")
    print(f"Largest in {sample_list3}: {find_largest(sample_list3)}")
    print(f"Largest in {sample_list4}: {find_largest(sample_list4)}")