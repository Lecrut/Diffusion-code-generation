import sys
def calculate_sum(data):
    total = 0
    for item in data:
        if isinstance(item, int):
            total += item
        else:
            pass
    return total
if __name__ == '__main__':
    sample_input = "10 20 30 hello 40 50"
    try:
        input_data = sample_input.split()
        numbers = []
        for item in input_data:
            try:
                numbers.append(int(item))
            except ValueError:
                pass
        result = calculate_sum(numbers)
        print(result)
    except Exception:
        pass