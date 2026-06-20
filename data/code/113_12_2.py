diff_table = {'A': (10.5, 4.2), 'B': (3.7, 1.8)}

def calculate_difference(key):
    return diff_table[key][0] - diff_table[key][1]

if __name__ == '__main__':
    result_A = calculate_difference('A')
    result_B = calculate_difference('B')
    print(f"Result for 'A': {result_A}")
    print(f"Result for 'B': {result_B}")