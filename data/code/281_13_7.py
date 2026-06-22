def sum_of_integers():
    numbers = [-10, -5, 0, 5, 10, 15]
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == '__main__':
    result = sum_of_integers()
    print(f"Sum of (-10, -5, 0, 5, 10, 15): {result}")