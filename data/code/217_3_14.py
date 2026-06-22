class Maximizer:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def compute_max(self):
        return (self.a + self.b) / 2 + abs((self.a - self.b)) / 4

if __name__ == '__main__':
    maximizer_instance = Maximizer(10, 7)
    print(maximizer_instance.compute_max())