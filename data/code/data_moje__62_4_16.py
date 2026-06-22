from math import isqrt

def find_divisors(value):
    limit = isqrt(value)
    first_half = [i for i in range(1, limit + 1) if value % i == 0]
    second_half = [value // d for d in first_half if d * d != value]
    second_half.reverse()
    return first_half + second_half

def get_divisors_of_60():
    return find_divisors(60)

if __name__ == '__main__':
    sample_number = 60
    divs = find_divisors(sample_number)
    print(divs)