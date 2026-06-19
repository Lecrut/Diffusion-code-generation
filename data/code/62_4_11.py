class SecondElementExtractor:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
    
    def get_second_element(self):
        try:
            first = next(self.iterator)
            second = next(self.iterator)
            return second
        except StopIteration:
            return None

if __name__ == '__main__':
    data1 = [10, 20, 30, 40]
    extractor1 = SecondElementExtractor(data1)
    print(extractor1.get_second_element())
    
    data2 = [5, 15]
    extractor2 = SecondElementExtractor(data2)
    print(extractor2.get_second_element())
    
    data3 = [1]
    extractor3 = SecondElementExtractor(data3)
    print(extractor3.get_second_element())
    
    data4 = []
    extractor4 = SecondElementExtractor(data4)
    print(extractor4.get_second_element())