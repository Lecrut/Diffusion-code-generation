class Maximizer:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    @staticmethod
    def compute_max(a, b):
        return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    maximizer_instance = Maximizer(5, 3)
    print(maximizer_instance.compute_max())