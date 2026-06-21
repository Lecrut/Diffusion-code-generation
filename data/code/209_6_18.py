SAMPLE_VALUES = [12, 24, 36]

def calculate_average(samples):
    return sum(samples) / len(samples)

if __name__ == '__main__':
    average = calculate_average(SAMPLE_VALUES)
    print(f"The average is: {average}")