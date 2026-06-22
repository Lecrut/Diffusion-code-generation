class MaxSquared:
    def __init__(self):
        self.max_value = max(x**2 for x in range(1, 101))

if __name__ == '__main__':
    finder = MaxSquared()
    print(finder.max_value)