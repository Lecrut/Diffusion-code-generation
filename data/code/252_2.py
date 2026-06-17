class QuantityComparer:
    def compare(self, a: int, b: int) -> dict:
        if a > b:
            return {"result": "a is greater than b", "a": a, "b": b}
        elif a < b:
            return {"result": "a is less than b", "a": a, "b": b}
        else:
            return {"result": "a is equal to b", "a": a, "b": b}
if __name__ == '__main__':
    comparer = QuantityComparer()
    val1 = 10
    val2 = 5
    result1 = comparer.compare(val1, val2)
    print(f"Comparing {val1} and {val2}: {result1}")
    val3 = 20
    val4 = 20
    result2 = comparer.compare(val3, val4)
    print(f"Comparing {val3} and {val4}: {result2}")
    val5 = 3
    val6 = 15
    result3 = comparer.compare(val5, val6)
    print(f"Comparing {val5} and {val6}: {result3}")