class StringChecker:
    def starts_with_a_or_b(self, strings):
        for s in strings:
            if s.startswith('A') or s.startswith('B'):
                return True
        return False

if __name__ == '__main__':
    sc = StringChecker()
    sample_strings1 = ['apple', 'banana', 'cherry']
    sample_strings2 = ['grape', 'melon', 'kiwi']
    result1 = sc.starts_with_a_or_b(sample_strings1)
    result2 = sc.starts_with_a_or_b(sample_strings2)
    print(f"Result for sample_strings1: {result1}")
    print(f"Result for sample_strings2: {result2}")