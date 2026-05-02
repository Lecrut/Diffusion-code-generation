import sys
if __name__ == '__main__':
    input_data = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    input_list = list(map(int, sys.stdin.read().split()))
    if not input_list:
        sorted_list = []
    else:
        sorted_list = sorted(input_list)
    print(*(sorted_list))