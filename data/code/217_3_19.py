class Maximizer:
    @staticmethod
    def compute_max(a, b):
        return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    result = Maximizer.compute_max(5, 3)
    print(result)