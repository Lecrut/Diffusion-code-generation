NUM_VALUES = 7

def calculate_sum(values):
    return sum(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50, 60, 70]
    result = calculate_sum(sample_values)
    print(f"Sum of {NUM_VALUES} integers: {result}")