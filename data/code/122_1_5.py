def calculate_average(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = (i for i in range(1000000))
    average = calculate_average(sample_data)
    print(f"The average is: {average}")