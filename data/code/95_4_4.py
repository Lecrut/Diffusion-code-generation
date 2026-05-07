def check_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0 and num % 2 == 0:
            count += 1
    return count >= 3
if __name__ == '__main__':
    sample_list1 = [2, 4, 6, 1, 3, 5]
    sample_list2 = [1, 3, 5, 7, 9]
    sample_list3 = [2, 4, 6, 8, 10]
    sample_list4 = [10, 20, 30]
    sample_list5 = [1, 2, 3, 4]
    print(f"Sample List 1: {check_numbers(sample_list1)}")
    print(f"Sample List 2: {check_numbers(sample_list2)}")
    print(f"Sample List 3: {check_numbers(sample_list3)}")
    print(f"Sample List 4: {check_numbers(sample_list4)}")
    print(f"Sample List 5: {check_numbers(sample_list5)}")