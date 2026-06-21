class NumberFinder:
    @staticmethod
    def get_largest_number(numbers):
        if not numbers:
            return None
        return max(numbers)

if __name__ == '__main__':
    test_cases = [
        [10, 5, 22, 8, 3],
        [-1, -5, -22, -8, -3],
        [1.5, 2.5, 0.5, 3.5],
        [],
        [42]
    ]
    
    for case in test_cases:
        result = NumberFinder.get_largest_number(case)
        print(f"Input: {case} | Largest Number: {result}")