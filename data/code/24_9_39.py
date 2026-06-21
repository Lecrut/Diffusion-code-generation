class NumberChecker:
    def check_negativity(self, value):
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = {
        'positive': [10, 25, 30],
        'negative': [-1, -10, -5],
        'zero': [0]
    }
    
    results = {key: [checker.check_negativity(val) for val in values] for key, values in sample_values.items()}
    print(results)