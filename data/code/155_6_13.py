INPUT_STRING = '10 20 30 40'

def sum_numbers(input_string):
    numbers = input_string.split()
    total_sum = sum((int(num_str) for num_str in numbers))
    return total_sum
if __name__ == '__main__':
    result = sum_numbers(INPUT_STRING)
    print(result)