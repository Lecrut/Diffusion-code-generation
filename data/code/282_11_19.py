INPUT_DATA = '10 20 30 40 50'

def calculate_total(numbers):
    try:
        return sum(numbers)
    except TypeError as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    numbers = []
    try:
        for item in INPUT_DATA.split():
            numbers.append(int(item))
        total_sum = calculate_total(numbers)
        print(total_sum)
    except ValueError:
        print('Error: Invalid input detected.')