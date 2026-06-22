A = 5
B = 3
C = 7

def find_the_middle_value_among_three_compare(a, b, c):
    return sorted([a, b, c])[1]
if __name__ == '__main__':
    middle_value = find_the_middle_value_among_three_compare(A, B, C)
    print(middle_value)