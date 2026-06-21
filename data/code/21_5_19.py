class Comparator:
    def __init__(self, x, y, z):
        self.values = [x, y, z]
    
    def find_max(self):
        current_max = self.values[0]
        for val in self.values[1:]:
            if val > current_max:
                current_max = val
        return current_max
    
    def print_largest(self):
        return f"the largest is {self.find_max()}"

if __name__ == '__main__':
    comp = Comparator(5, 12, 8)
    print(comp.print_largest())
    comp2 = Comparator(100, 99, 101)
    print(comp2.find_max())