import sys
if __name__ == '__main__':
    input_data = [2, 3, 4, 5]
    running_product = 1
    for number in input_data:
        running_product *= number
    print(running_product)