import sys
def calculate_mean(data):
    if not data:
        return None
    return sum(data) / len(data)
if __name__ == '__main__':
    input_data_str = "10 20 30 40 50"
    try:
        data = [float(x) for x in input_data_str.split()]
        mean_value = calculate_mean(data)
        if mean_value is not None:
            print(mean_value)
        else:
            print("No valid numerical data found.")
    except ValueError:
        print("Error: Input contained non-numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")