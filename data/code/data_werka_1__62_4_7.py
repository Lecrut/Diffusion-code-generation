class SecondElementGenerator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
    
    def generate(self):
        try:
            first = next(self.iterable)
            yield next(self.iterable)
        except StopIteration:
            return

if __name__ == '__main__':
    data1 = [10, 20, 30, 40]
    gen1 = SecondElementGenerator(data1)
    print(list(gen1.generate()))
    
    data2 = [5, 15]
    gen2 = SecondElementGenerator(data2)
    print(list(gen2.generate()))
    
    data3 = [1]
    gen3 = SecondElementGenerator(data3)
    print(list(gen3.generate()))
    
    data4 = []
    gen4 = SecondElementGenerator(data4)
    print(list(gen4.generate()))