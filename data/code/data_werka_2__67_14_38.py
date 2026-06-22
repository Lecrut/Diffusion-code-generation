def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be either integers or floating-point numbers.')
    return a + b

class SumService:
    def __init__(self):
        self.sample_cases = {
            'case1': {'a': 5, 'b': 3},
            'case2': {'a': 2.5, 'b': 4.7},
            'case3': {'a': -1, 'b': -1},
            'case4': {'a': 0, 'b': 0},
            'case5': {'a': 100, 'b': 200.5}
        }
    
    def run_samples(self):
        for key, case in self.sample_cases.items():
            result = add_numbers(case['a'], case['b'])
            print(f"Result of adding {case['a']} and {case['b']}: {result}")

if __name__ == '__main__':
    service = SumService()
    service.run_samples()