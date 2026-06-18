import sys
def is_positive(result):
    return result > 0 and isinstance(result, (int, float))
if __name__ == '__main__':
    samples = [10**6 - 5, -3.5, 0, True, False]
    for val in samples:
        try:
            if is_positive(val):
                print(f"{val} is positive")
            else:
                print(f"{val} is not positive or invalid")
        except Exception as e:
            pass