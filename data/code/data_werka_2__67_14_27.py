def compute_sum(a, b):
    return a + b

class SumComputer:
    def __init__(self, initial_a=0, initial_b=0):
        self.a = initial_a
        self.b = initial_b
    
    def set_first_value(self, a):
        self.a = a
    
    def set_second_value(self, b):
        self.b = b
    
    def get_sum(self):
        return compute_sum(self.a, self.b)

if __name__ == '__main__':
    computer = SumComputer()
    computer.set_first_value(10)
    computer.set_second_value(20)
    print(computer.get_sum())
    
    computer.set_first_value(5.5)
    computer.set_second_value(3.3)
    print(computer.get_sum())
    
    computer.set_first_value(-7)
    computer.set_second_value(-3)
    print(computer.get_sum())