class Divider:
    @staticmethod
    def divide_and_remainder(dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder

if __name__ == '__main__':
    divider_instance = Divider()
    result1 = divider_instance.divide_and_remainder(10, 3)
    print(f"Quotient: {result1[0]}, Remainder: {result1[1]}")
    result2 = divider_instance.divide_and_remainder(-15, 4)
    print(f"Quotient: {result2[0]}, Remainder: {result2[1]}")
    result3 = divider_instance.divide_and_remainder(20, 7)
    print(f"Quotient: {result3[0]}, Remainder: {result3[1]}")