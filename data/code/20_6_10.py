def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, -1, -2, 100, 101]
    for value in sample_values:
        print(f"is_even({value}) = {is_even(value)}")