def multiply_elements(t):
    return [num for num in t for _ in range(5)]

if __name__ == '__main__':
    sample_input = (4, 5)
    result = multiply_elements(sample_input)
    print(result)