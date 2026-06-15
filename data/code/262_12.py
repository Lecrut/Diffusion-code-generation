import random
sample_numbers = [15, -3, 88, 0, -42, 99, 1]
if __name__ == '__main__':
    input_list = []
    try:
        for item in sample_numbers:
            if not isinstance(item, int):
                raise ValueError("Input must be an integer.")
            input_list.append(item)
        if not input_list:
            print("The list is empty.")
        else:
            smallest = min(input_list)
            largest = max(input_list)
            print(f"Input List: {input_list}")
            print(f"Smallest value: {smallest}")
            print(f"Largest value: {largest}")
    except ValueError as e:
        print(f"Error processing input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")