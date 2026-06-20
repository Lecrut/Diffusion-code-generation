class LengthComparator:
    RELATIONSHIPS = [
        (lambda a, b: a > b, "greater"),
        (lambda a, b: a < b, "less"),
    ]

    def compare(self, length_a, length_b):
        for check, label in self.RELATIONSHIPS:
            if check(length_a, length_b):
                return f"{length_a} is {label} than {length_b}"
        return f"{length_a} is equal to {length_b}"

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.compare(10, 20))
    print(comparator.compare(5, 5))
    print(comparator.compare(100, 50))