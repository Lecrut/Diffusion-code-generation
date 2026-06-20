class NumberPartitioner:
    def partition_and_sort(self, numbers):
        evens = sorted([num for num in numbers if num % 2 == 0])
        odds = sorted([num for num in numbers if num % 2 != 0])
        return evens, odds

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    partitioner = NumberPartitioner()
    even_list, odd_list = partitioner.partition_and_sort(sample_numbers)
    print("Even numbers:", even_list)
    print("Odd numbers:", odd_list)