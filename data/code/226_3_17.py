def repeat_elements(t):
    return [num for num in t for _ in range(5)]

if __name__ == '__main__':
    sample_input = (1, 2, 3)
    print(repeat_elements(sample_input))