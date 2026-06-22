SAMPLE_VALUES = [1, 2, 3, 4, 5]

def reverse_list(lst):
    return lst[::-1]

if __name__ == '__main__':
    reversed_values = reverse_list(SAMPLE_VALUES)
    print(reversed_values)