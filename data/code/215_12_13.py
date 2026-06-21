MAX_VALUE = float('-inf')

def find_maximum(numbers):
    if not numbers:
        return None
    maximum = MAX_VALUE
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    sample_tuple = (3, -1, 99, 42)
    empty_list = []
    
    print(f"Maximum of {sample_list}: {find_maximum(sample_list)}")
    print(f"Maximum of {sample_tuple}: {find_maximum(sample_tuple)}")
    print(f"Maximum of empty list: {find_maximum(empty_list)}")