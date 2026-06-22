T = 3

def repeat_elements(elements):
    return elements * T

if __name__ == '__main__':
    sample_set = {1, 2, 3}
    repeated_set = repeat_elements(sample_set)
    print(repeated_set)