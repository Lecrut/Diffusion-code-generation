class IntegerReverser:
    def reverse(self, x: int) -> int:
        negative = x < 0
        digits = abs(x)
        reversed_num = 0
        
        while digits > 0:
            remainder = digits % 10
            reversed_num = reversed_num * 10 + remainder
            digits //= 10
        
        if negative:
            reversed_num *= -1
        
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num

if __name__ == '__main__':
    solver = IntegerReverser()
    print(solver.reverse(123))
    print(solver.reverse(-456))
    print(solver.reverse(1534236469))