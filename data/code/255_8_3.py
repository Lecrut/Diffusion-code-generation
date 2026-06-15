import sys
def find_maximum(data_string):
    try:
        numbers = [float(x.strip()) for x in data_string.split(',')]
        if not numbers:
            return None
        return max(numbers)
    except ValueError:
        return "Error: Invalid input. Please ensure all parts are numerical."
if __name__ == '__main__':
    sample_input = "10,5,22,8,30"
    result = find_maximum(sample_input)
    print(result)