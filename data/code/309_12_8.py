def sum_list(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total
if __name__ == '__main__':
    list1 = [1.5, 2.7, 3.0, 4.8]
    list2 = [-10.5, 5.2, 0.0, 1.3]
    empty_list = []
    single_element = [99.9]
    sum1 = sum_list(list1)
    sum2 = sum_list(list2)
    sum_empty = sum_list(empty_list)
    sum_single = sum_list(single_element)
    print(f"The sum of {list1} is: {sum1}")
    print(f"The sum of {list2} is: {sum2}")
    print(f"The sum of {empty_list} is: {sum_empty}")
    print(f"The sum of {single_element} is: {sum_single}")
    print("\nVerification using built-in sum():")
    print(f"Sum of {list1} using built-in: {sum(list1)}")
    print(f"Sum of {list2} using built-in: {sum(list2)}")