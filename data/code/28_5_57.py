class Comparator:
    STRICT_INEQUALITY_THRESHOLD = 0.0

    @staticmethod
    def compare_and_report(num1: float, num2: float) -> bool:
        return num1 > num2 + Comparator.STRICT_INEQUALITY_THRESHOLD

if __name__ == '__main__':
    result = Comparator.compare_and_report(7.2, 6.9)
    print(result)