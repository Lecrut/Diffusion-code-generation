class MinFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_minimum(self):
        if not self.numbers:
            raise ValueError("Input list cannot be empty")
        minimum = self.numbers[0]
        for number in self.numbers[1:]:
            if number < minimum:
                minimum = number
        return minimum

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    sample_list2 = [-10, 5, 0, -20, 100]
    sample_list3 = [7]
    sample_list4 = []

    finder1 = MinFinder(sample_list1)
    print(f"Minimum of {sample_list1}: {finder1.find_minimum()}")

    finder2 = MinFinder(sample_list2)
    print(f"Minimum of {sample_list2}: {finder2.find_minimum()}")

    finder3 = MinFinder(sample_list3)
    print(f"Minimum of {sample_list3}: {finder3.find_minimum()}")

    try:
        finder4 = MinFinder(sample_list4)
        print(f"Minimum of {sample_list4}: {finder4.find_minimum()}")
    except ValueError as e:
        print(e)