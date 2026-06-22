def reverse_integer(n: int) -> int:
    negative = n < 0
    num = abs(n)
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if negative:
        reversed_num = -reversed_num
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    if reversed_num > INT_MAX or reversed_num < INT_MIN:
        return 0
    return reversed_num

def main() -> None:
    sample_inputs = [123, -456, 120, 0, 1534236469]
    for num in sample_inputs:
        result = reverse_integer(num)
        print(result)
if __name__ == '__main__':
    main()