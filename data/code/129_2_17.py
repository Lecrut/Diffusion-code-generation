def partition_sort(numbers):
    even = sorted([n for n in numbers if n % 2 == 0])
    odd = sorted([n for n in numbers if n % 2 != 0])
    return even, odd

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    even, odd = partition_sort(sample_numbers)
    print("Even numbers:", even)
    print("Odd numbers:", odd)