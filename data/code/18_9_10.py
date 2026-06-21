def median_via_integer_division(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) // 2
    else:
        return sorted_numbers[mid]

if __name__ == '__main__':
    array1 = [3, 1, 2, 4, 5]
    array2 = [1, 2, 3, 4]
    array3 = [7, 2, 9, 1, 3, 8, 4]

    print(median_via_integer_division(array1))
    print(median_via_integer_division(array2))
    print(median_via_integer_division(array3))