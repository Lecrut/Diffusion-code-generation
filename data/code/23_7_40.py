def compare_and_report(list1, list2):
    def validate_input(lst):
        if not isinstance(lst, list):
            raise ValueError("Input must be a list.")
        if not all(isinstance(x, int) for x in lst):
            raise ValueError("All elements in the list must be integers.")

    validate_input(list1)
    validate_input(list2)

    sum1 = sum(list1)
    sum2 = sum(list2)

    if sum1 > sum2:
        return sum1, list1
    elif sum2 > sum1:
        return sum2, list2
    else:
        return sum1, None

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 5, 5, 50, 5]
    result = compare_and_report(list_a, list_b)
    print(result)