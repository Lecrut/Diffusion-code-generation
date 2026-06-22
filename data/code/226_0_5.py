numbers = [1, 2, 3, 4, 5]
def repeat_elements(sequence):
    for element in sequence:
        for _ in range(10):
            print(element)

if __name__ == '__main__':
    repeat_elements(numbers)