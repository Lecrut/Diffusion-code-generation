class NonDecreasingChecker:
    def __init__(self, arr):
        self.arr = arr

    def find_violations(self):
        violations = []
        for i in range(len(self.arr) - 1):
            if self.arr[i + 1] < self.arr[i]:
                violations.append((i, i + 1))
        return violations

if __name__ == '__main__':
    sample_array = [1.0, 3.0, 2.0, 5.0, 4.0, 6.0, 7.0]
    checker = NonDecreasingChecker(sample_array)
    result = checker.find_violations()
    for start, end in result:
        print(f"Indices: ({start}, {end})")