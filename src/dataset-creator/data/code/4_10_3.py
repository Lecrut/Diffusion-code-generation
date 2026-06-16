def determine_output(choice):
    try:
        if choice not in ['a', 'b', 'c']:
            return "Invalid option selected."
        if choice == 'a':
            result = 10 + 5 * 2 - 3 ** 2
            return f"Calculation for {choice}: {result}"
        elif choice == 'b':
            items = ['apple', 'banana', 'cherry']
            count = len(items)
            total_cost = sum([i * 1.5 for i in range(count)])
            return f"Details for {choice}: Count={count}, Total Cost=${total_cost:.2f}"
        else:                
            x, y = 4, -3
            z = (x ** y) + abs(x * y)
            return f"Result for {choice}: {z}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
if __name__ == '__main__':
    sample_choices = ['a', 'b', 'c']
    for choice in sample_choices:
        output = determine_output(choice)
        print(f"Input: '{choice}' -> Output:\n{output}")