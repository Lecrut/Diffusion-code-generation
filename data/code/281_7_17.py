MAX_NUMBERS = 10

def sum_numbers(**kwargs):
    total = 0
    count = 0
    for value in kwargs.values():
        if count < MAX_NUMBERS:
            total += value
            count += 1
    return total

if __name__ == '__main__':
    sample_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
    result = sum_numbers(**sample_values)
    print(result)