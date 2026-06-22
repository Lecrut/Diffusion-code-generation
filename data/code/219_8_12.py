class MaxSquared:
    def max_squared(self):
        return max(x**2 for x in range(1, 101))

if __name__ == '__main__':
    finder = MaxSquared()
    print(finder.max_squared())