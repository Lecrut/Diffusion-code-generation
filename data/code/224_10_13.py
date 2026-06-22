NUMBERS = [1.5, 2.5, 3.5]

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    mean_value = calculate_mean(NUMBERS)
    print(f"Mean of {NUMBERS}: {mean_value}")