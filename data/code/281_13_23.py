NUMBERS = [-10, -5, 0, 5, 10, 15]

def sum_of_integers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == '__main__':
    result = sum_of_integers(NUMBERS)
    print(f"Sum of ({NUMBERS}): {result}")