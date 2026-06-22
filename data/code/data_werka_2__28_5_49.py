class Comparator:
    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"
    EQUAL_TO = "equal_to"

    @staticmethod
    def compare(num1: float, num2: float) -> str:
        if num1 > num2:
            return Comparator.GREATER_THAN
        elif num1 < num2:
            return Comparator.LESS_THAN
        else:
            return Comparator.EQUAL_TO

def compare_and_report(num1: float, num2: float) -> bool:
    result = Comparator.compare(num1, num2)
    return result == Comparator.GREATER_THAN

if __name__ == '__main__':
    result = compare_and_report(7.0, 3.5)
    print(result)