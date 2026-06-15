import sys
def calculate_average(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    continue
        if not numbers:
            return None
        return sum(numbers) / len(numbers)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
if __name__ == '__main__':
    sample_filename = "sample_data.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10\n")
            f.write("20\n")
            f.write("30\n")
            f.write("40\n")
        average = calculate_average(sample_filename)
        if isinstance(average, str):
            print(average)
        else:
            print(f"The average is: {average}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")