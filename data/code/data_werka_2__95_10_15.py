class Validator:
    def combine_and_report(self, a, b, c):
        results = []
        if a <= 0:
            results.append(f"{a} is not positive")
        if a % 2 != 0:
            results.append(f"{a} is not even")
        if a >= 100:
            results.append(f"{a} is not less than 100")
        
        if b <= 0:
            results.append(f"{b} is not positive")
        if b % 2 != 0:
            results.append(f"{b} is not even")
        if b >= 100:
            results.append(f"{b} is not less than 100")
            
        if c <= 0:
            results.append(f"{c} is not positive")
        if c % 2 != 0:
            results.append(f"{c} is not even")
        if c >= 100:
            results.append(f"{c} is not less than 100")
            
        status = "All checks passed" if not results else "; ".join(results)
        
        return {
            "inputs": [a, b, c],
            "status": status
        }

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 20, 30)
    print(result)