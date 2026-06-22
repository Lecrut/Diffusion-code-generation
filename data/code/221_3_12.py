NUMBERS = [5, 2, 8]

def sort_numbers(numbers=NUMBERS):
    return sorted(numbers)

if __name__ == '__main__':
    result1 = sort_numbers()
    print(f"Sorted (5, 2, 8): {result1}")
    result2 = sort_numbers([-10, 0, 3])
    print(f"Sorted (-10, 0, 3): {result2}")
    result3 = sort_numbers([7, 7, 7])
    print(f"Sorted (7, 7, 7): {result3}")