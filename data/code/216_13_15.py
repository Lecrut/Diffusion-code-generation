class ValueFinder:
    def find_middle(self, data_list):
        n = len(data_list)
        if n == 0:
            return None
        middle_index = n // 2
        if n % 2 == 1:
            return data_list[middle_index]
        else:
            return (data_list[middle_index - 1] + data_list[middle_index]) / 2

if __name__ == '__main__':
    finder = ValueFinder()
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [10, 20, 30, 40]
    sample_single = [99]
    sample_empty = []
    
    print(f"Middle value of {sample_odd}: {finder.find_middle(sample_odd)}")
    print(f"Middle value of {sample_even}: {finder.find_middle(sample_even)}")
    print(f"Middle value of {sample_single}: {finder.find_middle(sample_single)}")
    print(f"Middle value of {sample_empty}: {finder.find_middle(sample_empty)}")