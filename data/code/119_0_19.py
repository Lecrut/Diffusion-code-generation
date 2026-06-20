class SwapHelper:
    def swap(self, a, b):
        return (b, a)

if __name__ == '__main__':
    helper = SwapHelper()
    x, y = 5, 10
    x, y = helper.swap(x, y)
    print(f"x: {x}, y: {y}")