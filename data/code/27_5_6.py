class Comparator:
    @staticmethod
    def are_unequal(a, b):
        return a != b
if __name__ == '__main__':
    obj = Comparator()
    val1 = 10
    val2 = 20
    result1 = obj.are_unequal(val1, val2)
    print(f"Are {val1} and {val2} unequal? {result1}")
    val3 = 5
    val4 = 5
    result2 = obj.are_unequal(val3, val4)
    print(f"Are {val3} and {val4} unequal? {result2}")
    val5 = "hello"
    val6 = "world"
    result3 = obj.are_unequal(val5, val6)
    print(f"Are '{val5}' and '{val6}' unequal? {result3}")