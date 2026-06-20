class FilterTuples:
    MIN_AGE = 18
    MAX_HEIGHT = 200

    @staticmethod
    def is_eligible(t):
        age, height, income = t
        return age >= FilterTuples.MIN_AGE and height <= FilterTuples.MAX_HEIGHT and income > 50000

if __name__ == '__main__':
    sample_tuples = [
        (22, 175, 60000),
        (17, 180, 49000),
        (30, 190, 75000),
        (25, 210, 55000)
    ]
    filtered_tuples = [t for t in sample_tuples if FilterTuples.is_eligible(t)]
    print(filtered_tuples)