def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return max(numbers)
if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 8, 15]
    result1 = find_largest(sample_list1)
    print(f"The largest number in {sample_list1} is: {result1}")
    sample_list2 = [-5, -1, -10, -3]
    result2 = find_largest(sample_list2)
    print(f"The largest number in {sample_list2} is: {result2}")
    sample_list3 = [42]
    result3 = find_largest(sample_list3)
    print(f"The largest number in {sample_list3} is: {result3}")
    sample_list4 = []
    try:
        result4 = find_largest(sample_list4)
        print(f"The largest number in {sample_list4} is: {result4}")
    except ValueError as e:
        print(f"Error for {sample_list4}: {e}")