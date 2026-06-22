class MaxFinder:
    def find_max(self, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        max_value = numbers[0]
        for number in numbers[1:]:
            if number > max_value:
                max_value = number
        return max_value

if __name__ == '__main__':
    finder = MaxFinder()
    sample_list_1 = [10, 5, 20, 8, 15]
    sample_list_2 = [-5, -1, -10, -3]
    sample_list_3 = [42]
    sample_list_4 = []
    print(f"Max in {sample_list_1}: {finder.find_max(sample_list_1)}")
    print(f"Max in {sample_list_2}: {finder.find_max(sample_list_2)}")
    print(f"Max in {sample_list_3}: {finder.find_max(sample_list_3)}")