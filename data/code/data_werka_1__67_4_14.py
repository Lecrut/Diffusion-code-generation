def compute_sum(a, b):
    return a + b

if __name__ == '__main__':
    numbers = {'first': 4, 'second': 6}
    result = compute_sum(numbers['first'], numbers['second'])
    print(result)