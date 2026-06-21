class NumberClassifier:
    PRIME = 'prime'
    COMPOSITE = 'composite'

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    @classmethod
    def classify_numbers(cls, numbers):
        result = {cls.PRIME: [], cls.COMPOSITE: []}
        for num in numbers:
            if cls.is_prime(num):
                result[cls.PRIME].append(num)
            else:
                result[cls.COMPOSITE].append(num)
        return result

if __name__ == '__main__':
    sample_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    classifier = NumberClassifier()
    classified_numbers = classifier.classify_numbers(sample_numbers)
    print(classified_numbers)