NUMBERS = [3.5, 2.1, 4.8, 6.7]

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    print(calculate_mean(NUMBERS))