import sys
if __name__ == '__main__':
    input_data = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    input_numbers = list(map(int, sys.stdin.read().split()))
    if not input_numbers:
        sorted_numbers = []
    else:
        sorted_numbers = sorted(input_numbers)
    print(*(sorted_numbers))