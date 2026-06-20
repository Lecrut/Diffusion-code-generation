class NumberSwapper:
    def swap(self, x, y):
        return (y, x)

if __name__ == '__main__':
    swapper = NumberSwapper()
    result1 = swapper.swap(7, 9)
    result2 = swapper.swap(-3, 0)
    print(result1)
    print(result2)