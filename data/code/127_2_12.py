class OddNumberDetector:
    @staticmethod
    def is_odd(number: int) -> bool:
        return number & 1 != 0

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in sample_numbers:
        result = OddNumberDetector.is_odd(num)
        print(f"Number: {num}, Is Odd: {result}")