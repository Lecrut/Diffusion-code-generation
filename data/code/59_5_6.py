class MiddleFinder:
    def __init__(self, sequence):
        self.sequence = sequence

    def find_middle_index(self):
        length = len(self.sequence)
        if length % 2 == 0:
            # For even length, return the lower middle index
            return length // 2 - 1
        else:
            # For odd length, return the middle index
            return length // 2

    def get_middle_element(self):
        index = self.find_middle_index()
        return self.sequence[index]

if __name__ == '__main__':
    sequence_odd = [1.0, 2.0, 3.0, 4.0, 5.0]
    sequence_even = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

    finder_odd = MiddleFinder(sequence_odd)
    finder_even = MiddleFinder(sequence_even)

    print("Middle index of odd sequence:", finder_odd.find_middle_index())
    print("Middle element of odd sequence:", finder_odd.get_middle_element())

    print("Middle index of even sequence:", finder_even.find_middle_index())
    print("Middle element of even sequence:", finder_even.get_middle_element())