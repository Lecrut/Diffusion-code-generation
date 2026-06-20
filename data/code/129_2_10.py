def partition_sort(numbers):
    even = sorted([num for num in numbers if num % 2 == 0])
    odd = sorted([num for num in numbers if num % 2 != 0])
    return even, odd

if __name__ == '__main__':
    sample_numbers = [34, 7, 23, 89, 10, 56]
    even, odd = partition_sort(sample_numbers)
    print("Even numbers:", even)
    print("Odd numbers:", odd)