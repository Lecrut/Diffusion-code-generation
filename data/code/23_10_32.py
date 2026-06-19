class ValueComparator:

    def compare_values(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            return ('greater',) if val1 > val2 else ('less',) if val1 < val2 else ('equal',)
        elif isinstance(val1, str) and isinstance(val2, str):
            return ('greater',) if val1 > val2 else ('less',) if val1 < val2 else ('equal',)
        else:
            raise ValueError('Both values must be either numeric or strings.')
if __name__ == '__main__':
    comparator = ValueComparator()
    print(comparator.compare_values(10, 5))
    print(comparator.compare_values('apple', 'banana'))
    print(comparator.compare_values(3.14, 3.14))