def partition_sort(numbers):
    evens = sorted(filter(lambda x: x % 2 == 0, numbers))
    odds = sorted(filter(lambda x: x % 2 != 0, numbers))
    return evens, odds

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    even_list, odd_list = partition_sort(sample_numbers)
    print("Even numbers:", even_list)
    print("Odd numbers:", odd_list)