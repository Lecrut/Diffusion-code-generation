import sys

class NumberAdder:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def get_sum(self):
        return self.a + self.b

if __name__ == '__main__':
    adder_instance = NumberAdder(15, 27)
    result = adder_instance.get_sum()
    sys.stdout.write(str(result))