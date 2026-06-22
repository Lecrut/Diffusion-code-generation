def calculate_sum(input_string):
    number_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    numbers = []
    current_number = ''
    for char in input_string:
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ''
    if current_number:
        numbers.append(int(current_number))
    return sum(numbers)
if __name__ == '__main__':
    sample_input = '10,25,3.5,40'
    result = calculate_sum(sample_input)
    print(result)