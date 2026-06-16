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
    numbers = input_string.split()
    even_numbers = check_evenness(numbers)
    print("Even numbers found:")
    for num in even_numbers:
        print(num)