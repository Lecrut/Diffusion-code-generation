def calculate_average(data_string):
    numbers = []
    try:
        parts = data_string.split(',')
        for part in parts:
            if part.strip():
                numbers.append(float(part.strip()))
            else:
                raise ValueError("Empty segment found")
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
    except ValueError:
        return "Error: Non-numeric input found"
    except Exception:
        return "Error: Invalid format"
if __name__ == '__main__':
    sample1 = "10,20,30,40"
    sample2 = "5.5,10.5,15"
    sample3 = "1,2,three,4"
    sample4 = ""
    sample5 = "100"
    print(f"Input: '{sample1}', Average: {calculate_average(sample1)}")
    print(f"Input: '{sample2}', Average: {calculate_average(sample2)}")
    print(f"Input: '{sample3}', Average: {calculate_average(sample3)}")
    print(f"Input: '{sample4}', Average: {calculate_average(sample4)}")
    print(f"Input: '{sample5}', Average: {calculate_average(sample5)}")