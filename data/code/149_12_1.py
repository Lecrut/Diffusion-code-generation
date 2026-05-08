def reverse_list(numbers):
    return numbers[::-1]
if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    try:
        input_list = [int(x) for x in sample_input.split()]
        reversed_list = reverse_list(input_list)
        print(reversed_list)
    except ValueError:
        print("Error: Invalid input. Please enter a list of integers.")