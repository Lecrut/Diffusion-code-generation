def calculate_average(data_string):
    numbers = []
    for item in data_string.split(','):
        try:
            numbers.append(float(item.strip()))
        except ValueError:
            return None
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_input = "10,20,30,40,error"
    average = calculate_average(sample_input)
    print(average)
    sample_input_2 = "5.5,10,15.5"
    average_2 = calculate_average(sample_input_2)
    print(average_2)
    sample_input_3 = "1,2,three,4"
    average_3 = calculate_average(sample_input_3)
    print(average_3)
    sample_input_4 = ""
    average_4 = calculate_average(sample_input_4)
    print(average_4)