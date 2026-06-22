import functools
COMPLEX_NUMBERS = [3 + 4j, 1 - 2j, 5 + 6j, 0 + 0j, -1 + 1j]

def find_min_real_part(numbers):
    return functools.reduce(lambda a, b: a if a.real < b.real else b, numbers)
if __name__ == '__main__':
    result = find_min_real_part(COMPLEX_NUMBERS)
    print(result)