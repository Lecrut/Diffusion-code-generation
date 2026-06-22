def sum_of_numbers():
    numbers = {
        'a': 0.1,
        'b': 0.2,
        'c': 0.3,
        'd': 0.4,
        'e': 0.5,
        'f': 0.6,
        'g': 0.7
    }
    return sum(numbers.values())

if __name__ == '__main__':
    print(sum_of_numbers())