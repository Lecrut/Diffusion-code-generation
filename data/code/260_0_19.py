class NumberSetComparer:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def compare(self):
        return [x for x in self.set1 if x > max(self.set2)] + [y for y in self.set2 if y > max(self.set1)]

if __name__ == '__main__':
    comparer = NumberSetComparer({5, 3, 9, 7}, {4, 6, 8, 10})
    result = comparer.compare()
    print(result)