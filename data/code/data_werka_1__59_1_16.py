class SequenceMiddleFinder:
    def __init__(self, sequence):
        self.sequence = sequence

    def find_middle(self):
        middle_index = len(self.sequence) // 2
        return self.sequence[middle_index]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple1 = (10, 20, 30, 40, 50)
    list2 = ['a', 'b', 'c']
    tuple2 = ('x', 'y', 'z')
    list3 = [100]
    tuple3 = (200,)
    
    finder1 = SequenceMiddleFinder(list1)
    finder2 = SequenceMiddleFinder(tuple1)
    finder3 = SequenceMiddleFinder(list2)
    finder4 = SequenceMiddleFinder(tuple2)
    finder5 = SequenceMiddleFinder(list3)
    finder6 = SequenceMiddleFinder(tuple3)
    
    print(finder1.find_middle())
    print(finder2.find_middle())
    print(finder3.find_middle())
    print(finder4.find_middle())
    print(finder5.find_middle())
    print(finder6.find_middle())