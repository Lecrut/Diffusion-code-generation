class Comparator:
    @staticmethod
    def are_unequal(a, b):
        return a != b
if __name__ == '__main__':
    obj = Comparator()
    val1 = 10
    val2 = 10
    val3 = 20
    result1 = obj.are_unequal(val1, val2)
    print(f"Comparing {val1} and {val2}: {result1}")
    result2 = obj.are_unequal(val1, val3)
    print(f"Comparing {val1} and {val3}: {result2}")