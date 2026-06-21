def sort_two_numbers(a, b):
    if a < b:
        return [a, b]
    else:
        return [b, a]
if __name__ == '__main__':
    sample_values = [3, 1]
    sorted_values = sort_two_numbers(*sample_values)
    print(sorted_values)