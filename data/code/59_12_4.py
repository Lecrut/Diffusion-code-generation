import statistics
def find_middle(data):
    if not data:
        return None
    middle_index = len(data) // 2
    if len(data) % 2 == 1:
        return data[middle_index]
    else:
        return f"The middle items are at indices {middle_index - 1} and {middle_index}"
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    if not sample_numbers:
        print("Input list is empty.")
    else:
        middle_result = find_middle(sample_numbers)
        print(middle_result)