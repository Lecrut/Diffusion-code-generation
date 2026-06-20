class ParitySorter:
    def partition_and_sort(self, numbers):
        even_numbers = [n for n in numbers if n % 2 == 0]
        odd_numbers = [n for n in numbers if n % 2 != 0]
        return sorted(even_numbers), sorted(odd_numbers)

if __name__ == '__main__':
    sorter = ParitySorter()
    sample_list_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    even_list_1, odd_list_1 = sorter.partition_and_sort(sample_list_1)
    print(f"Even List 1: {even_list_1}")
    print(f"Odd List 1: {odd_list_1}")

    sample_list_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    even_list_2, odd_list_2 = sorter.partition_and_sort(sample_list_2)
    print(f"Even List 2: {even_list_2}")
    print(f"Odd List 2: {odd_list_2}")

    sample_list_3 = []
    even_list_3, odd_list_3 = sorter.partition_and_sort(sample_list_3)
    print(f"Even List 3: {even_list_3}")
    print(f"Odd List 3: {odd_list_3}")