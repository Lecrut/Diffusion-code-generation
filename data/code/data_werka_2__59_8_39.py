class MiddleFinder:
    def __init__(self, sequence):
        if not sequence:
            raise ValueError("The sequence is empty")
        self.sequence = sequence

    def find_middle(self):
        middle_index = len(self.sequence) // 2
        return self.sequence[middle_index]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    finder1 = MiddleFinder(sample_list1)
    print(finder1.find_middle())

    sample_list2 = [10, 20, 30, 40, 50, 60]
    finder2 = MiddleFinder(sample_list2)
    print(finder2.find_middle())