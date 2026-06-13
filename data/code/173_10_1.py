def group_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return {"even": even_numbers, "odd": odd_numbers}
if __name__ == '__main__':
    unsorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = group_numbers(unsorted_list)
    print(result)