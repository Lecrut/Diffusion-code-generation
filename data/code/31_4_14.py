def square_area(side):
    return side * side

if __name__ == '__main__':
    sample_inputs = {'small': 3, 'medium': 7, 'large': 12}
    for key, value in sample_inputs.items():
        computed = square_area(value)
        print(key, value, computed)