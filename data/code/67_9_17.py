class Summator:
    def __init__(self, initial_a, initial_b):
        self.a = initial_a
        self.b = initial_b

    def set_values(self, new_a, new_b):
        self.a = new_a
        self.b = new_b

    def get_sum(self):
        return self.a + self.b

if __name__ == '__main__':
    summator = Summator(10, 20)
    print(summator.get_sum())
    summator.set_values(5, 15)
    print(summator.get_sum())