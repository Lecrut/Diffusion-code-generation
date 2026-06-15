def find_absolute_minimum(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            if not content:
                return None
            numbers = [float(x.strip()) for x in content.splitlines() if x.strip()]
            if not numbers:
                return None
            return min(numbers)
    except FileNotFoundError:
        return "Error: File not found"
    except ValueError:
        return "Error: Invalid number format in file"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_filename = "numbers.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10\n-5\n22\n0\n3.14")
        minimum = find_absolute_minimum(sample_filename)
        print(minimum)
    except Exception as e:
        print(f"Setup error: {e}")