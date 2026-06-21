NUMBERS = [12, 24, 36]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    average = calculate_average(NUMBERS)
    print(f"The average is: {average}")