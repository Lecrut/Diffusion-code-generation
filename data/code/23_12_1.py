class ValueComparator:
    def compare_values(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            if val1 > val2:
                return (val1, val2, "greater")
            elif val1 < val2:
                return (val1, val2, "less")
            else:
                return (val1, val2, "equal")
        elif isinstance(val1, str) and isinstance(val2, str):
            if val1 > val2:
                return (val1, val2, "greater")
            elif val1 < val2:
                return (val1, val2, "less")
            else:
                return (val1, val2, "equal")
        else:
            return (None, None, "error: unsupported types")
if __name__ == '__main__':
    comparator = ValueComparator()
    num1 = 10
    num2 = 5
    result_num = comparator.compare_values(num1, num2)
    print(f"Comparing {num1} and {num2}: {result_num}")
    num3 = 7.5
    num4 = 7.5
    result_num2 = comparator.compare_values(num3, num4)
    print(f"Comparing {num3} and {num4}: {result_num2}")
    str1 = "apple"
    str2 = "banana"
    result_str = comparator.compare_values(str1, str2)
    print(f"Comparing '{str1}' and '{str2}': {result_str}")
    str3 = "zebra"
    str4 = "ant"
    result_str2 = comparator.compare_values(str3, str4)
    print(f"Comparing '{str3}' and '{str4}': {result_str2}")
    mixed1 = 10
    mixed2 = "hello"
    result_mixed = comparator.compare_values(mixed1, mixed2)
    print(f"Comparing {mixed1} and '{mixed2}': {result_mixed}")