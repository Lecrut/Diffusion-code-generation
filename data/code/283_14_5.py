def all_even(numbers):
    return all(num % 2 == 0 for num in numbers)

if __name__ == '__main__':
    sample_list1 = [2, 4, 6, 8]
    sample_list2 = [2, 3, 4, 6]
    print(f"All elements in sample_list1 are even: {all_even(sample_list1)}")
    print(f"All elements in sample_list2 are even: {all_even(sample_list2)}")