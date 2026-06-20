DIVISIBILITY_3 = 3
DIVISIBILITY_5 = 5

def filter_transform(numbers):
    return (x * 2 for x in numbers if x % DIVISIBILITY_3 == 0 or x % DIVISIBILITY_5 == 0)
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_transform(sample_numbers)
    print(list(result))