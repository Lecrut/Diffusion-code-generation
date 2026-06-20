def partition_and_sort(numbers):
    evens = sorted(filter(lambda x: x % 2 == 0, numbers))
    odds = sorted(filter(lambda x: x % 2 != 0, numbers))
    return evens, odds

if __name__ == '__main__':
    sample_numbers = [7, 4, 1, 8, 5, 2]
    even_list, odd_list = partition_and_sort(sample_numbers)
    print("Even numbers:", even_list)
    print("Odd numbers:", odd_list)