class TriCheck:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_a_positive(self):
        return self.a > 0

    def is_b_even(self):
        return self.b % 2 == 0

    def is_c_divisible_by_a(self):
        if self.a == 0:
            return False
        return self.c % self.a == 0

    def check_all(self):
        return self.is_a_positive() and self.is_b_even() and self.is_c_divisible_by_a()

if __name__ == '__main__':
    obj = TriCheck(2, 4, 8)
    print(obj.check_all())
    print(obj.is_a_positive())
    print(obj.is_b_even())
    print(obj.is_c_divisible_by_a())