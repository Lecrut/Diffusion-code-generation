class NumberUtils:
    @staticmethod
    def is_odd(number: int) -> bool:
        return number & 1 != 0

if __name__ == '__main__':
    nums = [7, 10, 0, -3]
    for num in nums:
        print(f"Is {num} odd? {NumberUtils.is_odd(num)}")