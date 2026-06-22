from functools import reduce

def find_min_real_part(numbers):
    return reduce(lambda a, b: a if a.real < b.real else b, numbers)

if __name__ == '__main__':
    sample_numbers = [3 + 4j, 1 - 2j, 5 + 6j, 0 + 7j]
    print(find_min_real_part(sample_numbers))