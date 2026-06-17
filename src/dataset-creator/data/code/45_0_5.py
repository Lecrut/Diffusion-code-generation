import sys
def add_numbers(a: float, b: float) -> int:
    return int(a + b)
if __name__ == '__main__':
    try:
        sample_a = 10
        sample_b = 20.5
        result = add_numbers(sample_a, sample_b)
        print(result)
    except Exception as e:
        sys.stderr.write(f"Error occurred during calculation: {e}\n")