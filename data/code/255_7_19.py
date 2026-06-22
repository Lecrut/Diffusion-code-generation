def find_max_number(numbers):
    return max(map(float, numbers.split()))

if __name__ == '__main__':
    sample_string = "3.14159 2.71828 1.61803 4.0 0.5"
    print(find_max_number(sample_string))