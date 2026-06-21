def sum_of_numbers(numbers):
    total_sum = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError("All elements in the list must be numbers")
        total_sum += number
    return total_sum

if __name__ == '__main__':
    sample_list1 = [1, -2, 3, -4, 5]
    sample_list2 = [-10, 0, 5, -2.5]
    sample_list3 = [-1, -1, -1, -1]
    sample_list4 = [100]
    sample_list5 = []

    try:
        result1 = sum_of_numbers(sample_list1)
        print(f"Result for {sample_list1}: {result1}")
    except ValueError as e:
        print(e)

    try:
        result2 = sum_of_numbers(sample_list2)
        print(f"Result for {sample_list2}: {result2}")
    except ValueError as e:
        print(e)

    try:
        result3 = sum_of_numbers(sample_list3)
        print(f"Result for {sample_list3}: {result3}")
    except ValueError as e:
        print(e)

    try:
        result4 = sum_of_numbers(sample_list4)
        print(f"Result for {sample_list4}: {result4}")
    except ValueError as e:
        print(e)

    try:
        result5 = sum_of_numbers(sample_list5)
        print(f"Result for {sample_list5}: {result5}")
    except ValueError as e:
        print(e)