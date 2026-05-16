import sys
if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    numbers = list(map(int, input_data.split()))
    if not numbers:
        print("No numbers provided")
    else:
        n = len(numbers)
        if n % 2 == 1:
            middle_index = n // 2
            print(numbers[middle_index])
        else:
            print("Input has an even number of elements, no single middle element exists.")