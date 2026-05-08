def reverse_list(numbers):
    return numbers[::-1]
if __name__ == '__main__':
    sample_input = "1,5,3,9,2"
    try:
        input_list = [int(x.strip()) for x in sample_input.split(',')]
        reversed_list = reverse_list(input_list)
        print(reversed_list)
    except ValueError:
        print("Error: Invalid input. Please ensure all entries are integers separated by commas.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")