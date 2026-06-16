import sys
def calculate_sum(data):
    total = 0
    for item in data:
        try:
            total += int(item)
        except ValueError:
            pass
    return total
if __name__ == '__main__':
    input_data = [
        "10",
        "25",
        "hello",
        "3.5",
        "-5"
    ]
    result = calculate_sum(input_data)
    print(result)