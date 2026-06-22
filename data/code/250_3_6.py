NUMBERS = [10, 20, 30, 40]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    avg = calculate_average(NUMBERS)
    print(avg)