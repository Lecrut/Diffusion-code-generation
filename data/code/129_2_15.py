def partition_sort(numbers):
    evens = sorted([num for num in numbers if num % 2 == 0])
    odds = sorted([num for num in numbers if num % 2 != 0])
    return evens, odds

if __name__ == '__main__':
    sample_numbers = [34, 17, 23, 89, 56, 42]
    even_nums, odd_nums = partition_sort(sample_numbers)
    print("Even numbers:", even_nums)
    print("Odd numbers:", odd_nums)