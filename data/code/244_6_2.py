def calculate_area_sum(line1, line2):
    try:
        dims1 = line1.split()
        if len(dims1) != 2:
            raise ValueError("First line must contain exactly two dimensions.")
        length1 = float(dims1[0])
        width1 = float(dims1[1])
        area1 = length1 * width1
        dims2 = line2.split()
        if len(dims2) != 2:
            raise ValueError("Second line must contain exactly two dimensions.")
        length2 = float(dims2[0])
        width2 = float(dims2[1])
        area2 = length2 * width2
        return area1 + area2
    except ValueError as e:
        raise ValueError(f"Error processing input: {e}")
    except IndexError:
        raise ValueError("Input lines do not contain enough values.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    input_line1 = "10 5"
    input_line2 = "4 6"
    try:
        result = calculate_area_sum(input_line1, input_line2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")