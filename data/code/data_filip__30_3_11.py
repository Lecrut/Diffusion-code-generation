def int_to_binary(n):
    if n == 0:
        return '0'
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    if n == 0:
        return '0'
    bits = []
    while n > 0:
        if n & 1:
            bits.append('1')
        else:
            bits.append('0')
        n >>= 1
    if is_negative:
        ones_complement = []
        for b in bits:
            if b == '1':
                ones_complement.append('0')
            else:
                ones_complement.append('1')
        carry = 1
        twos_complement = []
        for i in range(len(ones_complement) - 1, -1, -1):
            bit = ones_complement[i]
            sum_val = (1 if bit == '1' else 0) + carry
            twos_complement.append(str(sum_val % 2))
            carry = sum_val // 2
        if carry:
            twos_complement.append('1')
        result = ''.join(reversed(twos_complement))
    else:
        result = ''.join(reversed(bits))
    return result

if __name__ == '__main__':
    print(int_to_binary(10))
    print(int_to_binary(0))
    print(int_to_binary(-10))
    print(int_to_binary(255))
    print(int_to_binary(1000000000000))