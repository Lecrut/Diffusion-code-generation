MAX_VALUE = float('-inf')

def find_max_element(numbers):
    global MAX_VALUE
    for number in numbers:
        if number > MAX_VALUE:
            MAX_VALUE = number
    return MAX_VALUE

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(find_max_element(sample_values))