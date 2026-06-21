def find_middle_item(numbers):
    def validate_input():
        if not numbers:
            raise ValueError("The list is empty")
    
    validate_input()
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35, 45]
    print(find_middle_item(sample_values))