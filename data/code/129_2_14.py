def partition_and_sort(numbers):
    evens = sorted([num for num in numbers if num % 2 == 0])
    odds = sorted([num for num in numbers if num % 2 != 0])
    return evens, odds

if __name__ == '__main__':
    sample_numbers = [34, 1, 98, 76, 5, 23, 89]
    even_nums, odd_nums = partition_and_sort(sample_numbers)
    print("Evens:", even_nums)
    print("Odds:", odd_nums)