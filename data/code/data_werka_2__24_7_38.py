class MathUtils:
    @staticmethod
    def is_negative(number):
        return number < 0

if __name__ == '__main__':
    test_cases = {
        'positive': [10, 23, 50],
        'negative': [-1, -5, -9.5],
        'zero': [0]
    }
    
    results = {}
    for category, values in test_cases.items():
        results[category] = {value: MathUtils.is_negative(value) for value in values}
    
    print(results)