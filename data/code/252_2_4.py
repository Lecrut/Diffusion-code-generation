class QuantityComparer:
    def compare(self, a: int, b: int) -> dict:
        result = {
            "a": a,
            "b": b,
            "comparison_result": "",
            "difference": a - b
        }
        if a > b:
            result["comparison_result"] = "a is greater than b"
        elif a < b:
            result["comparison_result"] = "a is less than b"
        else:
            result["comparison_result"] = "a is equal to b"
        return result
if __name__ == '__main__':
    comparer = QuantityComparer()
    value1 = 10
    value2 = 5
    comparison1 = comparer.compare(value1, value2)
    print(f"Comparing {value1} and {value2}: {comparison1}")
    value3 = 7
    value4 = 7
    comparison2 = comparer.compare(value3, value4)
    print(f"Comparing {value3} and {value4}: {comparison2}")
    value5 = 20
    value6 = 15
    comparison3 = comparer.compare(value5, value6)
    print(f"Comparing {value5} and {value6}: {comparison3}")