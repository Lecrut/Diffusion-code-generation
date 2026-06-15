class QuantityComparer:
    def __init__(self):
        pass
    def compare(self, a, b):
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
    print(result1)
    val3 = 7
    val4 = 7
    result2 = comparer.compare(val3, val4)
    print(result2)
    val5 = 20
    val6 = 15
    result3 = comparer.compare(val5, val6)
    print(result3)