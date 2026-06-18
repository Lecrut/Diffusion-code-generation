num = 17
is_odd = num % 2 != 0
print(f"{num} is odd: {bool(is_odd)}")

if __name__ == '__main__':
    test_values = [5, 4, 9]
    for val in test_values:
        result = val % 2 != 0
        print(f"Is {val} odd? {result}")