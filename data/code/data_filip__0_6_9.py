digit_map = {str(i): True for i in range(10)}

def count_digits(s):
    return sum(digit_map.get(c, False) for c in s)

if __name__ == '__main__':
    print(count_digits("test123abc456"))