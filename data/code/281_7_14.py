def calculate_sum(**kwargs):
    total = 0.0
    for value in kwargs.values():
        total += value
    return total

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 20,
        'c': 30,
        'd': -40,
        'e': 50,
        'f': 60,
        'g': 70,
        'h': -80,
        'i': 90,
        'j': 100
    }
    result = calculate_sum(**sample_values)
    print(result)