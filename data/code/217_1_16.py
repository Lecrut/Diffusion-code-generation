class NumberComparer:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def is_greater(self):
        if not isinstance(self.a, int) or not isinstance(self.b, int):
            raise TypeError('Both inputs must be integers')
        return self.a > self.b
if __name__ == '__main__':
    comparer1 = NumberComparer(10, 5)
    print(comparer1.is_greater())
    comparer2 = NumberComparer(20, 30)
    print(comparer2.is_greater())
    comparer3 = NumberComparer(7, 7)
    try:
        print(comparer3.is_greater())
    except TypeError as e:
        print(e)
    comparer4 = NumberComparer(-5, 12)
    print(comparer4.is_greater())