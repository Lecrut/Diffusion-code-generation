class TupleComparer:
    def compare(self, t1, t2):
        return t1 if t1 > t2 else t2

if __name__ == '__main__':
    comparer = TupleComparer()
    result1 = comparer.compare((3, 4), (2, 5))
    result2 = comparer.compare(('apple', 'banana'), ('banana', 'cherry'))
    print(result1)
    print(result2)