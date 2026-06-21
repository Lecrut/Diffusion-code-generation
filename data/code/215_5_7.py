def find_highest_value(lst):
    return max(lst, key=lambda x: x)

if __name__ == '__main__':
    sample_values = [-5, -10, -2, -8, -1]
    print(find_highest_value(sample_values))