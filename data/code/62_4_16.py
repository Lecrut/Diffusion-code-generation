class SecondElementIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
    
    def get_second_element(self):
        try:
            first = next(self.iterator)
            second = next(self.iterator)
            return [second]
        except StopIteration:
            return []

if __name__ == '__main__':
    data1 = [10, 20, 30, 40]
    iter1 = SecondElementIterator(data1)
    print(iter1.get_second_element())
    
    data2 = [5, 15]
    iter2 = SecondElementIterator(data2)
    print(iter2.get_second_element())
    
    data3 = [1]
    iter3 = SecondElementIterator(data3)
    print(iter3.get_second_element())
    
    data4 = []
    iter4 = SecondElementIterator(data4)
    print(iter4.get_second_element())