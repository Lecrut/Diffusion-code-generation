import sys
def check_evenness(numbers):
    even_numbers = []
    for num in numbers:
        if isinstance(num, int):
            if num % 2 == 0:
                even_numbers.append(num)
    return even_numbers
if __name__ == '__main__':
    input_string = "1 2 3 4 5 6 7 8 9 10"
    try:
        numbers = [int(x) for x in input_string.split()]
        result = check_evenness(numbers)
        print(*(result))
    except ValueError:
        print("Error: One or more inputs were not valid integers.", file=sys.stderr)