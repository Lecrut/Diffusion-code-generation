def partition_sort(numbers):
    even = sorted([num for num in numbers if num % 2 == 0])
    odd = sorted([num for num in numbers if num % 2 != 0])
    return even, odd

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    even, odd = partition_sort(sample_numbers)
    print("Even:", even)
    print("Odd:", odd)