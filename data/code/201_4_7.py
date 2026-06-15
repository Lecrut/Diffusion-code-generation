def calculate_average(data_string):
    numbers = []
    parts = data_string.split(',')
    for part in parts:
        try:
            numbers.append(float(part.strip()))
        except ValueError:
            return None
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_input = "10,20,30,40,error"
    average = calculate_average(sample_input)
    print(f"The average is: {average}")
    sample_input_2 = "5.5,10,15,20"
    average_2 = calculate_average(sample_input_2)
    print(f"The average of '{sample_input_2}' is: {average_2}")
    sample_input_3 = "1,2,three,4"
    average_3 = calculate_average(sample_input_3)
    print(f"The average of '{sample_input_3}' is: {average_3}")
    sample_input_4 = ""
    average_4 = calculate_average(sample_input_4)
    print(f"The average of '{sample_input_4}' is: {average_4}")