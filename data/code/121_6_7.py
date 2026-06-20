class TupleComparer:
    @staticmethod
    def compare(tup1, tup2):
        return tup1 if tup1 > tup2 else tup2

if __name__ == '__main__':
    result = TupleComparer.compare((3, 4), (2, 5))
    print(result)