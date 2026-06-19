class NumberAdder:
    @staticmethod
    def add_numbers(a, b):
        try:
            return float(a) + float(b)
        except (ValueError, TypeError):
            raise ValueError("Both inputs must be numbers")

if __name__ == '__main__':
    result1 = NumberAdder.add_numbers(5, 10)
    print(result1)
    
    result2 = NumberAdder.add_numbers(20.5, 3.2)
    print(result2)
    
    try:
        result3 = NumberAdder.add_numbers("a", 10)
        print(result3)
    except ValueError as e:
        print(e)