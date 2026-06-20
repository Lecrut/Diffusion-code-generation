def partition_and_sort(numbers):
    evens = sorted([num for num in numbers if num % 2 == 0])
    odds = sorted([num for num in numbers if num % 2 != 0])
    return evens, odds

if __name__ == '__main__':
    sample_numbers = [10, 3, 5, 8, 2, 7, 1]
    even_list, odd_list = partition_and_sort(sample_numbers)
    print("Even numbers:", even_list)
    print("Odd numbers:", odd_list)