class BothFalseGenerator:
    def __init__(self, a: bool, b: bool):
        self.a = a
        self.b = b

    def generate(self):
        if not self.a and not self.b:
            yield True

if __name__ == '__main__':
    gen1 = BothFalseGenerator(False, False)
    print(next(gen1.generate()))
    
    gen2 = BothFalseGenerator(True, False)
    print(next(gen2.generate()))
    
    gen3 = BothFalseGenerator(False, True)
    print(next(gen3.generate()))
    
    gen4 = BothFalseGenerator(True, True)
    try:
        print(next(gen4.generate()))
    except StopIteration:
        print("StopIteration as expected")