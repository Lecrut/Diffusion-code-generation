def sum_of_numbers():
    numbers = {
        'one': 0.1,
        'two': 0.2,
        'three': 0.3,
        'four': 0.4,
        'five': 0.5,
        'six': 0.6,
        'seven': 0.7
    }
    return sum(numbers.values())

if __name__ == '__main__':
    print(sum_of_numbers())