class BitwiseCounter:
    @staticmethod
    def count_and_check_exclusive(a: bool, b: bool, c: bool, d: bool, e: bool) -> bool:
        return (a + b + c + d + e) == 1

if __name__ == '__main__':
    result = BitwiseCounter.count_and_check_exclusive(True, False, True, False, False)
    print(result)