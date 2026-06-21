class MiddleFinder:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_middle(self):
        length = len(self.sequence)
        if length == 0:
            raise ValueError("Sequence must not be empty")
        index = (length - 1) // 2
        return self.sequence[index]

if __name__ == '__main__':
    finder_odd = MiddleFinder([10, 20, 30, 40, 50])
    print(finder_odd.get_middle())
    
    finder_even = MiddleFinder([100, 200, 300, 400])
    print(finder_even.get_middle())
    
    finder_single = MiddleFinder([99])
    print(finder_single.get_middle())
    
    finder_large_even = MiddleFinder([1, 2, 3, 4, 5, 6])
    print(finder_large_even.get_middle())