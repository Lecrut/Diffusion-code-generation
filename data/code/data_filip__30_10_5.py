def integer_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    
    return "".join(reversed(bits))

if __name__ == '__main__':
    sample_values = [0, 1, 5, 10, 255, 1024]
    for val in sample_values:
        print(integer_to_binary(val))