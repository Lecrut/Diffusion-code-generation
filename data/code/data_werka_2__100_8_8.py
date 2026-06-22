class NumberComparator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def calculate_sum(self):
        return self.first + self.second

    def calculate_difference(self):
        return self.first - self.second

    def check_condition(self):
        s = self.calculate_sum()
        d = self.calculate_difference()
        return s > d

if __name__ == '__main__':
    comp = NumberComparator(20, 15)
    s_val = comp.calculate_sum()
    d_val = comp.calculate_difference()
    cond = comp.check_condition()
    print(s_val)
    print(d_val)
    print(cond)