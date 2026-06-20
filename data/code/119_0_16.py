class SwapUtil:
    @staticmethod
    def swap(a, b):
        a, b = b, a
        return a, b

if __name__ == '__main__':
    util = SwapUtil()
    x, y = 5, 10
    x, y = util.swap(x, y)
    print(f"x: {x}, y: {y}")