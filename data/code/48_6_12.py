import operator

def find_max(*numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if operator.gt(num, max_val):
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_values = (42, 17, 89, 3, 102, 55)
    result = find_max(*sample_values)
    print(result)