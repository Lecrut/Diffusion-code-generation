class LargestNumberFinder:
    def find_largest(self, numbers):
        if not numbers:
            return None
        largest = numbers[0]
        for number in numbers[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    finder = LargestNumberFinder()
    sample_list = [10, 5, 20, 8, 15]
    print(f"Largest in {sample_list}: {finder.find_largest(sample_list)}")