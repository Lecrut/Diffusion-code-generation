numbers = {
    'negative_ten': -10,
    'negative_five': -5,
    'zero': 0,
    'positive_five': 5,
    'positive_ten': 10,
    'positive_fifteen': 15
}

def sum_of_integers():
    total = 0
    for num in numbers.values():
        total += num
    return total

if __name__ == '__main__':
    result = sum_of_integers()
    print(f"Sum of (-10, -5, 0, 5, 10, 15): {result}")