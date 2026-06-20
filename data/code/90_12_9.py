class StringEvaluator:
    def check_strings(self, strings):
        for s in strings:
            if s.startswith('A') or s.startswith('B'):
                return True
        return False

if __name__ == '__main__':
    se = StringEvaluator()
    sample1 = ['apple', 'banana']
    sample2 = ['carrot', 'date']
    sample3 = ['avocado', 'blueberry']
    sample4 = ['grape', 'kiwi']

    result1 = se.check_strings(sample1)
    result2 = se.check_strings(sample2)
    result3 = se.check_strings(sample3)
    result4 = se.check_strings(sample4)

    print(f"Result for sample1: {result1}")
    print(f"Result for sample2: {result2}")
    print(f"Result for sample3: {result3}")
    print(f"Result for sample4: {result4}")