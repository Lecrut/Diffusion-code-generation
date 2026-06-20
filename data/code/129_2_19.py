def partition_sort(numbers):
    evens = sorted([num for num in numbers if num % 2 == 0])
    odds = sorted([num for num in numbers if num % 2 != 0])
    return evens, odds

if __name__ == '__main__':
    sample_numbers = [34, 1, 56, 78, 9, 23, 45]
    even_list, odd_list = partition_sort(sample_numbers)
    print("Even numbers:", even_list)
    print("Odd numbers:", odd_list)