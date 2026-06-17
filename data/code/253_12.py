class MedianFinder:
    def get_middle(self, a, b, c):
        numbers = sorted([a, b, c])
        return numbers[1]
if __name__ == '__main__':
    mf = MedianFinder()
    a_val = 5
    b_val = 2
    c_val = 8
    result = mf.get_middle(a_val, b_val, c_val)
    print(result)