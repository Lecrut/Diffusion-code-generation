class OddNumberDetector:
    BITWISE_AND_MASK = 1

    @staticmethod
    def is_odd(number: int) -> bool:
        return (number & OddNumberDetector.BITWISE_AND_MASK) != 0

if __name__ == '__main__':
    numbers_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in numbers_to_check:
        result = OddNumberDetector.is_odd(num)
        print(f"Number: {num}, Is Odd: {result}")