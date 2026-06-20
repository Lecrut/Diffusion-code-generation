class PartitionSort:
    def __init__(self):
        self.partitioned_lists = []

    def partition_and_sort(self, int_list):
        even_numbers = [x for x in int_list if x % 2 == 0]
        odd_numbers = [x for x in int_list if x % 2 != 0]
        
        sorted_even = sorted(even_numbers)
        sorted_odd = sorted(odd_numbers)
        
        self.partitioned_lists.extend([sorted_even, sorted_odd])

    def get_partitioned_lists(self):
        return self.partitioned_lists

if __name__ == '__main__':
    ps = PartitionSort()
    
    sample_list_1 = [2, 3, 5, 8, 13, 21]
    ps.partition_and_sort(sample_list_1)
    print(f"Partitioned and Sorted List 1: {ps.get_partitioned_lists()}")
    
    sample_list_2 = [4, 9, 16, 25, 36, 49]
    ps.partition_and_sort(sample_list_2)
    print(f"Partitioned and Sorted List 2: {ps.get_partitioned_lists()}")