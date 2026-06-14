class NumberComparer:
    def compare(self, a, b):
        if a > b:
            return ("larger", "smaller")
        elif a < b:
            return ("smaller", "larger")
        else:
            return ("equal", "equal")
if __name__ == '__main__':
    comparer = NumberComparer()
    num1 = 10
    num2 = 5
    result = comparer.compare(num1, num2)
    print(f"Comparing {num1} and {num2}: {result}")
    num3 = 20
    num4 = 20
    result2 = comparer.compare(num3, num4)
    print(f"Comparing {num3} and {num4}: {result2}")
    num5 = 3
    num6 = 7
    result3 = comparer.compare(num5, num6)
    print(f"Comparing {num5} and {num6}: {result3}")