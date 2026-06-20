def partition_sort(numbers):
    evens = sorted([n for n in numbers if n % 2 == 0])
    odds = sorted([n for n in numbers if n % 2 != 0])
    return evens, odds

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    even_nums, odd_nums = partition_sort(sample_numbers)
    print("Evens:", even_nums)
    print("Odds:", odd_nums)