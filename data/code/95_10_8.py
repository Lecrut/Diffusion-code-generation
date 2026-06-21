class Validator:
    def combine_and_report(self, a, b, c):
        results = []
        if a <= 0:
            results.append("a is not positive")
        if a % 2 != 0:
            results.append("a is not even")
        if a >= 100:
            results.append("a is too large")
        
        if b <= 0:
            results.append("b is not positive")
        if b % 2 != 0:
            results.append("b is not even")
        if b >= 100:
            results.append("b is too large")
            
        if c <= 0:
            results.append("c is not positive")
        if c % 2 != 0:
            results.append("c is not even")
        if c >= 100:
            results.append("c is too large")
            
        if not results:
            status = "All inputs are positive, even, and less than 100"
        else:
            status = "; ".join(results)
            
        return {
            "inputs": [a, b, c],
            "status": status
        }

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 20, 30)
    print(result)