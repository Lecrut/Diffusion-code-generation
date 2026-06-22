NUMBERS = [-10, -5, 0, 5, 10, 15]

def sum_of_integers():
    total = 0
    for num in NUMBERS:
        total += num
    return total

if __name__ == '__main__':
    result = sum_of_integers()
    print(f"Sum of {NUMBERS}: {result}")