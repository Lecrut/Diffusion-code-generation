def sum_ten_numbers(**kwargs):
    total = 0.0
    for number in kwargs.values():
        total += number
    return total

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 20,
        'c': 30,
        'd': -5,
        'e': 15,
        'f': 25,
        'g': 35,
        'h': -20,
        'i': 40,
        'j': 50
    }
    result = sum_ten_numbers(**sample_values)
    print(result)